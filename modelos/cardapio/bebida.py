from modelos.cardapio.item_cardapio import ItemCardapio

class bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def __str__(self):
        return f'Bebida: {self._nome}, Preço: R${self._preco:.2f}, Tamanho: {self.tamanho}'