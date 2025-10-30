from models.usuario import Usuario

class Empresa(Usuario):
    def __init__(self, id_usuario, nome, username, email, senha, tipo, nome_empresa, cnpj):
        super().__init__(id_usuario, nome, username, email, senha, tipo)
        self.nome_empresa = nome_empresa
        self.cnpj = cnpj