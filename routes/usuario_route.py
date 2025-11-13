from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services.usuario_services import UsuarioService
from utils.mensagens_erros import ERROS

usuario_bp = Blueprint('usuarios', __name__)

@usuario_bp.route('/', methods=['GET'])
@jwt_required()
def listar_usuarios():
    usuarios = UsuarioService.listar_usuarios()
    return jsonify(usuarios), 200

@usuario_bp.route('/<int:id_usuario>', methods=['GET'])
@jwt_required()
def buscar_usuario_por_id(id_usuario):
    usuario = UsuarioService.buscar_usuario_por_id(id_usuario)
    if usuario == ERROS["USUARIO_NAO_ENCONTRADO"]:
        return jsonify(usuario), 404
    return jsonify(usuario), 200

@usuario_bp.route("/", methods=["POST"])
def criar_usuario():
    dados = request.get_json()
    obrigatorios = ["username", "nome", "email", "senha", "categoria"]

    if not all(campo in dados for campo in obrigatorios):
        return jsonify({"mensagem": "Campos obrigatórios ausentes."}), 400

    resultado = UsuarioService.criar_usuario(
        username=dados["username"],
        nome=dados["nome"],
        email=dados["email"],
        senha=dados["senha"],
        tipo=dados["categoria"]
    )

    status = resultado.get("status", 201)
    return jsonify(resultado), status


@usuario_bp.route("/<int:id_usuario>", methods=["PUT"])
@jwt_required()
def atualizar_usuario(id_usuario):
    dados = request.get_json()
    resultado = UsuarioService.atualizar_usuario(
        id_usuario=id_usuario,
        nome=dados.get("nome"),
        username=dados.get("username"),
        email=dados.get("email"),
        senha=dados.get("senha"),
        tipo=dados.get("categoria")
    )

    if resultado is None:
        return jsonify({"message": "Usuário atualizado com sucesso"}), 200
    return jsonify(resultado), resultado.get("status", 400)


@usuario_bp.route("/<int:id_usuario>", methods=["DELETE"])
@jwt_required()
def deletar_usuario(id_usuario):
    resultado = UsuarioService.deletar_usuario(id_usuario)
    if resultado is None:
        return jsonify({"message": "Usuário deletado com sucesso"}), 200

    return jsonify(resultado), resultado.get("status", 400)



