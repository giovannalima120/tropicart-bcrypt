from dao.usuario_dao import UsuarioDAO
from utils.mensagens_erros import ERROS


class UsuarioService:
    @staticmethod
    def listar_usuarios():
        return UsuarioDAO.get_all_users()

    @staticmethod
    def buscar_usuario_por_id(id_usuario):
        usuario = UsuarioDAO.get_user_by_id(id_usuario)
        if not usuario:
            return ERROS["USUARIO_NAO_ENCONTRADO"]
        return usuario
    
    @staticmethod
    def buscar_usuario_por_email(email):
        usuario = UsuarioDAO.get_user_by_email(email)
        return usuario
    
    @staticmethod
    def buscar_usuario_por_username(username):
        usuario = UsuarioDAO.get_user_by_username(username)
        return usuario
    
    @staticmethod
    def criar_usuario(nome, username, email, senha, tipo):
        if UsuarioDAO.get_user_by_email(email):
            return ERROS["EMAIL_DUPLICADO"]
        if UsuarioDAO.get_user_by_username(username):
            return ERROS["USERNAME_DUPLICADO"]
        
        user_id = UsuarioDAO.insert_user(nome, username, email, senha, tipo)
        return user_id
    
    @staticmethod
    def atualizar_usuario(id_usuario, nome, username, email, senha, tipo):
        usuario = UsuarioDAO.get_user_by_id(id_usuario)
        if not usuario:
            return ERROS["USUARIO_NAO_ENCONTRADO"]
        
        usuario_encontrado = UsuarioDAO.get_user_by_username(username)
        if usuario_encontrado and usuario_encontrado['id_usuario'] != id_usuario:
            return ERROS["USERNAME_DUPLICADO"]
        
        email_encontrado = UsuarioDAO.get_user_by_email(email)
        if email_encontrado and email_encontrado['id_usuario'] != id_usuario:
            return ERROS["EMAIL_DUPLICADO"]
        
        UsuarioDAO.update_user(id_usuario, nome, username, email, senha, tipo)

    @staticmethod
    def deletar_usuario(id_usuario):
        usuario = UsuarioDAO.get_user_by_id(id_usuario)
        if not usuario:
            return ERROS["USUARIO_NAO_ENCONTRADO"]
        UsuarioDAO.delete_user(id_usuario)
        