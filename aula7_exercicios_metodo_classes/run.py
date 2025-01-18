class Loja:

    taxa = 1.15

    def __init__(self, valor:float):
        self.valor_produto_bruto = valor

    def consultar_valor_produto(self):
        valor_produto = self.valor_produto_bruto * self.taxa
        print(f"Valor: {valor_produto}")

    @classmethod
    def alterar_taxa_produto(cls, valor: float):
        cls.taxa = valor
        #Loja.taxa = valor


loja_praia = Loja(44.2)
loja_shopping = Loja(71.10)
loja_rua = Loja(11.10)

loja_praia.consultar_valor_produto()
loja_shopping.consultar_valor_produto()
loja_rua.consultar_valor_produto()

loja_shopping.alterar_taxa_produto(1.40)
print("Pós Taxa:")

loja_praia.consultar_valor_produto()
loja_shopping.consultar_valor_produto()
loja_rua.consultar_valor_produto()