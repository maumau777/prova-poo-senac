from pizzaria.pizza import Pizza, PizzaEspecial

def criar_pizza():
    nome = input("Digite o sabor da pizza (ex: Margherita, Calabresa): ")
    tamanho = input("Digite o tamanho da pizza (Pequena, Média, Grande): ")
    return Pizza(nome, tamanho)

def criar_pizza_especial():
    nome = input("Digite o sabor da pizza especial (ex: Margherita, Calabresa): ")
    tamanho = input("Digite o tamanho da pizza (Pequena, Média, Grande): ")
    adicionais = []
    while True:
        adicional = input("Digite um adicional (ou 'sair' para finalizar): ")
        if adicional.lower() == 'sair':
            break
        adicionais.append(adicional)
    return PizzaEspecial(nome, tamanho, adicionais)
