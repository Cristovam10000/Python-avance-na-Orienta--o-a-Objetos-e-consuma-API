from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome,preco)
        self.descricao = descricao

    def __str__(self):
        return f'Prato: {self._nome}, Preço: R${self._preco:.2f}, Descrição: {self.descricao}'

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)  # Aplica um desconto de 8% no preço do prato