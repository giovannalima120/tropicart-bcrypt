from models.usuario import Usuario

class Artista(Usuario):
    def __init__ (self, id_usuario, nome, username, email, senha, tipo, area):
        super().__init__(id_usuario, nome, username, email, senha, tipo)
        self.area = area
