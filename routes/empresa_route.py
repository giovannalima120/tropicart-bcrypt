from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services.empresa_service import EmpresaService
from utils.mensagens_erros import ERROS

empresa_bp = Blueprint('empresas', __name__)

@empresa_bp.route('/', methods=['GET'])
@jwt_required()
def listar_empresas():
    empresas = EmpresaService.listar_empresas()
    return jsonify(empresas), 200

@empresa_bp.route('/<int:id_empresa>', methods=['GET'])
@jwt_required()
def buscar_empresa(id_empresa):
    empresa = EmpresaService.buscar_empresa_por_id(id_empresa)
    if empresa == ERROS["EMPRESA_NAO_ENCONTRADA"]:
        return jsonify(empresa), 404
    return jsonify(empresa), 200

@empresa_bp.route("/", methods=["POST"])
@jwt_required()
def criar_empresa():
    dados = request.get_json()
    resultado = EmpresaService.criar_empresa(
        id_usuario=dados["id_usuario"],
        nome_empresa=dados["nome_empresa"],
        cnpj=dados["cnpj"]
    )
    status = resultado.get("status", 201)
    return jsonify(resultado), status


@empresa_bp.route("/<int:id_empresa>", methods=["PUT"])
@jwt_required()
def atualizar_empresa(id_empresa):
    dados = request.get_json()
    resultado = EmpresaService.atualizar_empresa(
        id_empresa=id_empresa,
        nome_empresa=dados.get("nome_empresa"),
        cnpj=dados.get("cnpj")
    )

    status = resultado.get("status", 200)
    return jsonify(resultado), status


@empresa_bp.route("/<int:id_empresa>", methods=["DELETE"])
@jwt_required()
def deletar_empresa(id_empresa):
    resultado = EmpresaService.deletar_empresa(id_empresa)
    status = resultado.get("status", 200)
    return jsonify(resultado), status



