

class veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado  = False

    def __str__(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ligado: {self._ligado}'


class carro(veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def __str__(self):
        return f'{super().__str__()}, Portas: {self.portas}'


class moto(veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def __str__(self):
        return f'{super().__str__()}, Tipo: {self.tipo}'