
class Banco:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

class Agencia(Banco):
    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self.numero = numero
