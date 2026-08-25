from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import bebida
from modelos.cardapio.prato import Prato

# teste
from modelos.Pratica.Veiculo import veiculo
from modelos.Pratica.Veiculo import carro
from modelos.Pratica.Veiculo import moto

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida1 = bebida('Coca-Cola', 5.00, 'grande')
bebida1.aplicar_desconto()
prato1 = Prato('Lasanha', 25.00, 'Lasanha de carne com molho branco e queijo gratinado')
prato1.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida1)
restaurante_praca.adicionar_no_cardapio(prato1)

# teste
veiculo1 = veiculo('Toyota', 'Corolla')
carro1 = carro('Honda', 'Civic', 4)
moto1 = moto('Yamaha', 'MT-07', 'Esportiva')





def main():
    restaurante_praca.exibir_cardapio

    # teste
    print(veiculo1)
    print(carro1)
    print(moto1)

if __name__ == '__main__':
    main()