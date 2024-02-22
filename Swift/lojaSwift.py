produtos = ("Pão de queijo 400g", "Salsicha Hot-dog 500g", "Pão de alho baguete 400g", "Filé de peito frango 1KG", "Isca de Frango 300g", "Linguiça toscana 700g", "Pedaço de Filé de Salmão 500g", "Filé de Tilápia 250g", "Bife de Filé Mignon MAIS 900g", "Carne moída patinho 900g")
precos = (10.76, 9.96, 10.96, 19.96, 13.96, 17.96, 54.96, 13.96, 89.96, 39.97)

def menu(produtos, precos):
    for i in range(len(produtos)):
        print(f'{produtos[i]:.<40}{precos[i]}')

def mostrarPreco(escolha):
    for i in range(len(produtos)):
        if produtos[i].__contains__(escolha):
           print(f'{produtos[i]:.<40}{precos[i]}')


def mostrarNome(escolha):
    minimo = min(precos)
    maximo = max(precos)
    for preco in precos:
        if preco >= escolha and preco < maximo:
            maximo = preco
        if preco < escolha and preco > minimo:
            minimo = preco
    return (maximo, minimo)
 

while True:
    print('Produtos................................Preços')
    print(menu(produtos, precos))
    escolhaFiltro = int(input('Qual filtro você deseja utilizar? \n1-Por nome do produto\n2-Por preço\n'))
    if escolhaFiltro == 1:
        escolha_Produto = str(input('Qual produtodeseja? '))
        print(mostrarPreco(escolha_Produto))
    elif escolhaFiltro == 2:
        escolhaPreco = float(input('Qual você deseja? '))
        print(mostrarNome(escolhaPreco))
    else:
        print('Escolha uma opção válida.')
    continuar = int(input('Deseja continuar? (1-SIM; 2-NÃO) '))
    if continuar == 1:
        continue
    else:
        print('OK! Até a próxima')
        break


