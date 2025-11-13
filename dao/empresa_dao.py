from database.connection import get_connection
from models.empresa import Empresa

class EmpresaDAO:
    @staticmethod
    def criar_empresa(empresa: Empresa):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            INSERT INTO empresas (id_usuario, nome_empresa, cnpj)
            VALUES (?, ?, ?);
            ''',
            (empresa.id_usuario, empresa.nome_empresa, empresa.cnpj)
        )
        conn.commit()
        conn.close()
        return empresa.id_usuario
    
    @staticmethod
    def listar_empresas():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM empresas;
            '''
        )
        empresas = cursor.fetchall()
        empresaDict = [dict(e) for e in empresas]
        conn.close()
        return empresaDict
    
    @staticmethod
    def buscar_empresa_por_id(id_empresa):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM empresas WHERE id_usuario = ?;
            ''',
            (id_empresa,)
        )
        resultado = cursor.fetchone()
        conn.close()
        if resultado is None:
            return None
        return dict(resultado)
    
    @staticmethod
    def buscar_empresa_por_cnpj(cnpj):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM empresas WHERE cnpj = ?;
            ''',
            (cnpj, )
        )
        resultado = cursor.fetchone()
        conn.close()
        if resultado is None:
            return None
        return dict(resultado)
    
    @staticmethod
    def atualizar_empresa(id_empresa, nome_empresa, cnpj):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            UPDATE empresas
            SET nome_empresa = ?, cnpj = ?
            WHERE id_usuario = ?;
            ''',
            (nome_empresa, cnpj, id_empresa)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def deletar_empresa(id_empresa):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            DELETE FROM empresas WHERE id_usuario = ?;
            ''',
            (id_empresa,)
        )
        conn.commit()
        conn.close()