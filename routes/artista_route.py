from models.artista import Artista
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services.artista_service import ArtistaService
from utils.mensagens_erros import ERROS

artista_bp = Blueprint('artistas', __name__)

@artista_bp.route('/', methods=['GET'])
@jwt_required()
def listar_artistas():
    artistas = ArtistaService.listar_artistas()
    return jsonify(artistas), 200

@artista_bp.route('/<int:id_artista>', methods=['GET'])
@jwt_required()
def buscar_artista(id_artista):
    artista = ArtistaService.buscar_artista_por_id(id_artista)
    if artista == ERROS["ARTISTA_NAO_ENCONTRADO"]:
        return jsonify(artista), 404
    return jsonify(artista), 200

@artista_bp.route("/", methods=["POST"])
@jwt_required()
def criar_artista():
    dados = request.get_json()
    artista = Artista(id_usuario=dados["id_usuario"], area=dados["area"])
    resultado = ArtistaService.criar_artista(artista)
    status = resultado.get("status", 201)
    return jsonify(resultado), status


@artista_bp.route("/<int:id_artista>", methods=["PUT"])
@jwt_required()
def atualizar_artista(id_artista):
    dados = request.get_json()
    resultado = ArtistaService.atualizar_artista(
        id_artista=id_artista,
        area=dados.get("area")
    )

    status = resultado.get("status", 200)
    return jsonify(resultado), status


@artista_bp.route("/<int:id_artista>", methods=["DELETE"])
@jwt_required()
def deletar_artista(id_artista):
    resultado = ArtistaService.deletar_artista(id_artista)
    status = resultado.get("status", 200)
    return jsonify(resultado), status



