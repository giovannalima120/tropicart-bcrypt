from database.connection import get_connection
from models.artista import Artista

class ArtistaDAO:
    @staticmethod
    def criar_artista(artista):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            INSERT INTO artistas (id_usuario, area)
            VALUES (?, ?);
            ''',
            (artista.id_usuario, artista.area)
        )
        conn.commit()
        conn.close()
    
    @staticmethod
    def listar_artistas():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM artistas;
            '''
        )
        artistas = cursor.fetchall()
        artistaDict = [dict(a) for a in artistas]
        conn.close()
        return artistaDict
    
    @staticmethod
    def buscar_artista_por_id(id_artista):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM artistas WHERE id_usuario = ?;
            ''',
            (id_artista,)
        )
        artista = dict(cursor.fetchone())
       
        conn.close()
        if artista is None:
            return None
        return dict(artista)
    
    @staticmethod
    def buscar_artista_por_username(username):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM artistas WHERE username = ?;
            ''',
            (username,)
        )
        artista = dict(cursor.fetchone())
        conn.close()
        return artista
    
    
    @staticmethod
    def atualizar_artista(id_artista, area):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            UPDATE artistas
            SET area = ?
            WHERE id_usuario = ?;
            ''',
            (area, id_artista)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def deletar_artista(id_artista):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            DELETE FROM artistas WHERE id_usuario = ?;
            ''',
            (id_artista,)
        )
        conn.commit()
        conn.close()