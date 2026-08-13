from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('João', 5)
restaurante_praca.receber_avaliacao('Maria', 4)
restaurante_praca.receber_avaliacao('Pedro', 3)
restaurante_mexicano = Restaurante('mexicano', 'Fast Food')
restaurante_italiano = Restaurante('italiano', 'Fast Food')

def main():
    Restaurante.listar_restaurantes()
    restaurante_praca.listar_avaliacao()

if __name__ == '__main__':
    main()