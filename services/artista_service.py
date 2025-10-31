from dao.artista_dao import ArtistaDAO
from models.artista import Artista
from utils.mensagens_erros import ERROS

class ArtistaService:
    @staticmethod
    def listar_artistas():
        return ArtistaDAO.listar_artistas()

    @staticmethod
    def buscar_artista_por_id(id_artista):
        artista = ArtistaDAO.buscar_artista_por_id(id_artista)
        if not artista:
            return ERROS["ARTISTA_NAO_ENCONTRADO"]
        return artista
    
    @staticmethod
    def criar_artista(artista: Artista):
        if ArtistaDAO.buscar_artista_por_id(artista.id_usuario):
            return ERROS["ARTISTA_JA_EXISTE"]
    
        ArtistaDAO.criar_artista(artista)

    @staticmethod
    def atualizar_artista(id_artista, area):
        artista = ArtistaDAO.buscar_artista_por_id(id_artista)
        if not artista:
            return ERROS["ARTISTA_NAO_ENCONTRADO"]
        ArtistaDAO.atualizar_artista(id_artista, area)
    
    @staticmethod
    def deletar_artista(id_artista):
        artista = ArtistaDAO.buscar_artista_por_id(id_artista)
        if not artista:
            return ERROS["ARTISTA_NAO_ENCONTRADO"]
        ArtistaDAO.deletar_artista(id_artista)