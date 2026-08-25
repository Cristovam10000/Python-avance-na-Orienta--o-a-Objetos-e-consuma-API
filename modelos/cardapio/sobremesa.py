from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, descricao, tipo, tamanho):
        super().__init__(nome, preco)
        self._descricaao = descricao
        self._tipo = tipo
        self._tamanho = tamanho

    def __str__(self):
        return f'Sobremesa: {self._nome}, Preço: R${self._preco:.2f}, Descrição: {self._descricaao}, Tipo: {self._tipo}, Tamanho: {self._tamanho}'

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.10)  # Aplica um desconto de 10% no preço da sobremesa