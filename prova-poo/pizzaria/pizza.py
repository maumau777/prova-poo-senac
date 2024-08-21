class Pizza:
    # Dicionário de preços pré-definidos por tamanho
    precos_base = {
        "Pequena": 30.0,
        "Média": 50.0,
        "Grande": 70.0
    }

    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho
        self.preco = self.precos_base.get(tamanho, 0.0)  # Obtém o preço base a partir do tamanho da pizza

    def calcular_preco(self):
        return self.preco

    def exibir_detalhes(self):
        print(f"Pizza: {self.nome} - Tamanho: {self.tamanho} - Preço: R${self.calcular_preco()}")

class PizzaEspecial(Pizza):
    def __init__(self, nome, tamanho, adicionais=None):
        super().__init__(nome, tamanho)
        self.adicionais = adicionais if adicionais else []

    def calcular_preco(self):
        preco_final = super().calcular_preco()
        preco_adicionais = len(self.adicionais) * 3
        return preco_final + preco_adicionais

    def exibir_detalhes(self):
        super().exibir_detalhes()
        if self.adicionais:
            print("Adicionais:")
            for adicional in self.adicionais:
                print(f"- {adicional}")
