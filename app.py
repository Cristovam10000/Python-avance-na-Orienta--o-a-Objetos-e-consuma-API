from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import bebida
from modelos.cardapio.prato import Prato

# teste
from modelos.Pratica.Veiculo import veiculo
from modelos.Pratica.Veiculo import carro
from modelos.Pratica.Veiculo import moto

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida1 = bebida('Coca-Cola', 5.00, 'grande')
prato1 = Prato('Lasanha', 25.00, 'Lasanha de carne com molho branco e queijo gratinado')

# teste
veiculo1 = veiculo('Toyota', 'Corolla')
carro1 = carro('Honda', 'Civic', 4)
moto1 = moto('Yamaha', 'MT-07', 'Esportiva')





def main():
    print(restaurante_praca)
    print(bebida1)
    print(prato1)

    # teste
    print(veiculo1)
    print(carro1)
    print(moto1)

if __name__ == '__main__':
    main()