from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services.vaga_service import VagaService
from utils.mensagens_erros import ERROS

vaga_bp = Blueprint('vagas', __name__)

@vaga_bp.route('/', methods=['GET'])
@jwt_required()
def listar_vagas():
    vagas = VagaService.listar_vagas()
    return jsonify(vagas), 200

@vaga_bp.route('/<int:id_vaga>', methods=['GET'])
@jwt_required()
def buscar_vaga(id_vaga):
    vaga = VagaService.buscar_vaga_por_id(id_vaga)
    if vaga == ERROS["VAGA_NAO_ENCONTRADA"]:
        return jsonify(vaga), 404
    return jsonify(vaga), 200

@vaga_bp.route("/", methods=["POST"])
@jwt_required()
def criar_vaga():
    dados = request.get_json()

    obrigatorios = ["titulo", "salario", "descricao", "requisitos"]
    if not dados or any(campo not in dados for campo in obrigatorios):
        return jsonify({"error": "Dados incompletos"}), 400
    
    vaga_id = VagaService.criar_vaga(
        titulo=dados["titulo"],
        salario=dados["salario"],
        descricao=dados["descricao"],
        requisitos=dados["requisitos"],
        id_empresa=dados["id_empresa"]
    )

    if isinstance(vaga_id, dict) and "status" in vaga_id:
        return jsonify(vaga_id), vaga_id["status"]
    
    return jsonify({"message": "Vaga criada com sucesso", "id_vaga": vaga_id}), 201


@vaga_bp.route("/<int:id_vaga>", methods=["PUT"])
@jwt_required()
def atualizar_vaga(id_vaga):
    dados = request.get_json()
    resultado = VagaService.atualizar_vaga(
        id_vaga=id_vaga,
        titulo=dados.get("titulo"),
        salario=dados.get("salario"),
        descricao=dados.get("descricao"),
        requisitos=dados.get("requisitos")
    )

    status = resultado.get("status", 200)
    return jsonify(resultado), status


@vaga_bp.route("/<int:id_vaga>", methods=["DELETE"])
@jwt_required()
def deletar_vaga(id_vaga):
    resultado = VagaService.deletar_vaga(id_vaga)
    status = resultado.get("status", 200)
    return jsonify(resultado), status



