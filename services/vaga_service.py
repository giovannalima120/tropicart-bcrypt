from dao.empresa_dao import EmpresaDAO
from dao.vaga_dao import VagaDAO
from models.vaga import Vaga
from utils.mensagens_erros import ERROS

class VagaService:
    @staticmethod
    def listar_vagas():
        return VagaDAO.listar_vagas()

    @staticmethod
    def buscar_vaga_por_id(id_vaga):
        vaga = VagaDAO.buscar_vaga_por_id(id_vaga)
        if not vaga:
            return ERROS["VAGA_NAO_ENCONTRADA"]
        return vaga
    
    @staticmethod
    def criar_vaga(titulo, salario, descricao, requisitos, id_empresa):

        empresa = EmpresaDAO.buscar_empresa_por_id(id_empresa)
        if not empresa:
            return ERROS["EMPRESA_NAO_ENCONTRADA"]
        
        nova_vaga = Vaga(
            id_vaga=None,
            titulo=titulo,
            salario=salario,
            descricao=descricao,
            requisitos=requisitos,
            id_empresa=id_empresa
        )
        vaga_id = VagaDAO.criar_vaga(nova_vaga)
        return {"message": "Vaga criada com sucesso", "id": vaga_id, "status": 201}

    @staticmethod
    def atualizar_vaga(id_vaga, titulo, salario, descricao, requisitos):
        vaga = VagaDAO.buscar_vaga_por_id(id_vaga)
        if not vaga:
            return ERROS["VAGA_NAO_ENCONTRADA"]
        
        VagaDAO.atualizar_vaga(id_vaga, titulo, salario, descricao, requisitos)

    @staticmethod
    def deletar_vaga(id_vaga):
        VagaDAO.deletar_vaga(id_vaga)
        return {"message": "Vaga deletada com sucesso", "status": 200}