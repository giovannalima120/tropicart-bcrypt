import sqlite3
from database.connection import get_connection


def criar_tabelas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS usuarios (
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            tipo TEXT NOT NULL
        )'''
    )
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS empresas (
            id_usuario INTEGER PRIMARY KEY,
            nome_empresa TEXT NOT NULL,
            cnpj TEXT NOT NULL UNIQUE,
            FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario)
        )'''
    )
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS artistas (
            id_usuario INTEGER PRIMARY KEY,
            area TEXT NOT NULL,
            FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario)
        )'''
    )
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS vagas (
            id_vaga INTEGER PRIMARY KEY AUTOINCREMENT,
            id_empresa INTEGER NOT NULL,
            titulo TEXT NOT NULL,
            salario REAL NOT NULL,
            descricao TEXT NOT NULL,
            requisitos TEXT NOT NULL,
            FOREIGN KEY (id_empresa) REFERENCES empresas (id_usuario)
        )'''
    )

    conn.commit()
    conn.close()

    if __name__ == '__main__':
        criar_tabelas()