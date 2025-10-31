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
        nova_vaga = Vaga(
            id_vaga=None,
            titulo=titulo,
            salario=salario,
            descricao=descricao,
            requisitos=requisitos,
            id_empresa=id_empresa
        )
        VagaDAO.criar_vaga(nova_vaga)

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