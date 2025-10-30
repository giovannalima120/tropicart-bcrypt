from dao.empresa_dao import EmpresaDAO
from utils.mensagens_erros import ERROS

class EmpresaService:
    @staticmethod
    def listar_empresas():
        return EmpresaDAO.listar_empresas()

    @staticmethod
    def buscar_empresa_por_id(id_empresa):
        empresa = EmpresaDAO.buscar_empresa_por_id(id_empresa)
        if not empresa:
            return ERROS["EMPRESA_NAO_ENCONTRADA"]
        return empresa
    
    @staticmethod
    def criar_empresa(id_usuario, nome_empresa, cnpj):
        if EmpresaDAO.buscar_empresa_por_id(id_usuario):
            return ERROS["EMPRESA_JA_EXISTE"]
        
        if EmpresaDAO.buscar_empresa_por_cnpj(cnpj):
            return ERROS["CNPJ_DUPLICADO"]
        
        EmpresaDAO.criar_empresa(id_usuario, nome_empresa, cnpj)

    @staticmethod
    def atualizar_empresa(id_empresa, nome_empresa, cnpj):
        empresa = EmpresaDAO.buscar_empresa_por_id(id_empresa)
        if not empresa:
            return ERROS["EMPRESA_NAO_ENCONTRADA"]
        
        cnpj_encontrado = EmpresaDAO.buscar_empresa_por_cnpj(cnpj)
        if cnpj_encontrado and cnpj_encontrado['id_empresa'] != id_empresa:
            return ERROS["CNPJ_DUPLICADO"]
        
        EmpresaDAO.atualizar_empresa(id_empresa, nome_empresa, cnpj)
    
    @staticmethod
    def deletar_empresa(id_empresa):
        empresa = EmpresaDAO.buscar_empresa_por_id(id_empresa)
        if not empresa:
            return ERROS["EMPRESA_NAO_ENCONTRADA"]
        EmpresaDAO.deletar_empresa(id_empresa)