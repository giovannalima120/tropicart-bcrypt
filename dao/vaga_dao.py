from database.connection import get_connection
from models.vaga import Vaga

class VagaDAO:
    @staticmethod
    def criar_vaga(vaga: Vaga):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            INSERT INTO vagas (titulo, salario, descricao, requisitos, id_empresa)
            VALUES (?, ?, ?, ?, ?);
            ''',
            (vaga.titulo, vaga.salario, vaga.descricao, vaga.requisitos, vaga.id_empresa) 
        )
        conn.commit()
        conn.close()

    @staticmethod
    def listar_vagas():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM vagas;
            '''
        )
        vagas = cursor.fetchall()
        vagaDict = [dict(v) for v in vagas]
        conn.close()
        return vagaDict
    
    @staticmethod
    def buscar_vaga_por_id(id_vaga):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM vagas WHERE id_vaga = ?;
            ''',
            (id_vaga,)
        )
        vaga = dict(cursor.fetchone())
        conn.close()
        if vaga is None:
            return None
        return dict(vaga)
    
    @staticmethod
    def atualizar_vaga(id_vaga, titulo, salario, descricao, requisitos):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            UPDATE vagas
            SET titulo = ?, salario = ?, descricao = ?, requisitos = ?
            WHERE id_vaga = ?;
            ''',
            (titulo, salario, descricao, requisitos, id_vaga)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def deletar_vaga(id_vaga):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            DELETE FROM vagas WHERE id_vaga = ?;
            ''',
            (id_vaga,)
        )
        conn.commit()
        conn.close()