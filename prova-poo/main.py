from pizzaria.pedido import Pedido
from pizzaria.utils import criar_pizza, criar_pizza_especial

def main():
    numero_pedido = int(input("Digite o número do pedido: "))
    pedido = Pedido(numero_pedido)

    while True:
        tipo_pizza = input("Você quer adicionar uma pizza comum ou especial? (comum/especial/sair): ")
        if tipo_pizza.lower() == 'comum':
            pizza = criar_pizza()
            pedido.adicionar_pizza(pizza)
        elif tipo_pizza.lower() == 'especial':
            pizza = criar_pizza_especial()
            pedido.adicionar_pizza(pizza)
        elif tipo_pizza.lower() == 'sair':
            break
        else:
            print("Opção inválida. Tente novamente.")

    pedido.exibir_detalhes_pedido()

if __name__ == "__main__":
    main()
