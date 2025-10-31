from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash
from services.usuario_services import UsuarioService
from models.artista import Artista
from services.artista_service import ArtistaService
from services.empresa_service import EmpresaService

auth_bp = Blueprint('auth', __name__)
blacklist = set() 

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    obrigatorios = ["username", "nome", "email", "senha", "categoria"]
    if not data or any(campo not in data for campo in obrigatorios):
        return jsonify({"error": "Dados incompletos"}), 400

    if UsuarioService.buscar_usuario_por_email(data['email']):
        return jsonify({"error": "Email já cadastrado"}), 409
    if UsuarioService.buscar_usuario_por_username(data['username']):
        return jsonify({"error": "Username já cadastrado"}), 409

    hashed_password = generate_password_hash(data['senha'])

    usuario_id = UsuarioService.criar_usuario(
        username=data['username'],
        nome=data['nome'],
        email=data['email'],
        senha=hashed_password,
        tipo=data['categoria']
    )

    if data['categoria'] == 'artista':
        novo_artista = Artista(id_usuario=usuario_id, area=data.get("area", "Não informada"))
        ArtistaService.criar_artista(novo_artista)


    return jsonify({"message": "Usuário registrado com sucesso"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('senha'):
        return jsonify({"error": "Dados incompletos"}), 400

    usuario = UsuarioService.buscar_usuario_por_email(data['email'])
    if not usuario or not check_password_hash(usuario['senha'], data['senha']):
        return jsonify({"error": "Credenciais inválidas"}), 401

    access_token = create_access_token(identity=str(usuario['id_usuario']))
    return jsonify({"token": access_token}), 200

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    blacklist.add(jti)
    return jsonify({"message": "Logout realizado com sucesso"}), 200
