from abc import ABC, abstractmethod


class veiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado  = False

    def __str__(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ligado: {self._ligado}'

    @abstractmethod
    def ligar(self):
        pass


class carro(veiculo):
    def __init__(self, marca, modelo, portas, cor):
        super().__init__(marca, modelo)
        self.portas = portas
        self._cor = cor

    def __str__(self):
        return f'{super().__str__()}, Portas: {self.portas}'

    def ligar(self):
        self._ligado = True


class moto(veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def __str__(self):
        return f'{super().__str__()}, Tipo: {self.tipo}'

    def ligar(self):
        self._ligado = True