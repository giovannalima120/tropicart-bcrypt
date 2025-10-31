from database.connection import get_connection
from models.usuario import Usuario

class UsuarioDAO:
    @staticmethod
    def insert_user(nome, username, email, senha, tipo):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            INSERT INTO usuarios (nome, username, email, senha, tipo)
            VALUES (?, ?, ?, ?, ?);
            ''',
            (nome, username, email, senha, tipo)
        )
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return user_id

    @staticmethod

    def get_all_users():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM usuarios;
            '''
        )
        usuarios = cursor.fetchall()
        usuarioDict = [dict(u) for u in usuarios]
        conn.close()
        return usuarioDict

    @staticmethod
    def get_user_by_id(id_usuario):
        conn = get_connection()
        cursor = conn.cursor()  
        cursor.execute(
            '''
            SELECT * FROM usuarios WHERE id_usuario = ?;
            ''',
            (id_usuario,)
        )
        resultado = cursor.fetchone()
        conn.close()
        if resultado is None:
            return None
        return dict(resultado)
    
    @staticmethod
    def get_user_by_username(username):
        conn = get_connection()
        cursor = conn.cursor()  
        cursor.execute(
            '''
            SELECT * FROM usuarios WHERE username = ?;
            ''',
            (username,)
        )
        resultado = cursor.fetchone()
        conn.close()
        if resultado is None:
            return None
        return dict(resultado)
    @staticmethod
    def get_user_by_email(email):
        conn = get_connection()
        cursor = conn.cursor()  
        cursor.execute(
            '''
            SELECT * FROM usuarios WHERE email = ?;
            ''',
            (email,)
        )
        resultado = cursor.fetchone()
        conn.close()
        if resultado is None:
            return None
        return dict(resultado)
    
    @staticmethod
    def update_user(id_usuario, nome, username, email, senha, tipo):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            UPDATE usuarios
            SET nome = ?, username =?, email = ?, senha = ?, tipo = ?
            WHERE id_usuario = ?;
            ''',
            (nome, username, email, senha, tipo, id_usuario)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def delete_user(id_usuario):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            DELETE FROM usuarios WHERE id_usuario = ?;
            ''',
            (id_usuario,)
        )
        conn.commit()
        conn.close()