from pizzaria.pizza import Pizza, PizzaEspecial

class Pedido:
    def __init__(self, numero_pedido):
        self.numero_pedido = numero_pedido
        self.pizzas = []

    def adicionar_pizza(self, pizza):
        self.pizzas.append(pizza)

    def calcular_total(self):
        total = sum(pizza.calcular_preco() for pizza in self.pizzas)
        return total

    def exibir_detalhes_pedido(self):
        print(f"Pedido Nº: {self.numero_pedido}")
        for pizza in self.pizzas:
            pizza.exibir_detalhes()
        print(f"Total do Pedido: R${self.calcular_total()}")
