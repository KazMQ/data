import pandas as pd

produtos = ["Notebook", "Smartphone", "Tablet", "Smartwatch", "Camera"]
qtd_estoque = [15, 30, 20, 10, 25]

#Criando uma serie no Pandas
estoque = pd.Series(qtd_estoque, index=produtos)

#Exibindo a serie
print("Série Estoque de produtos: ")
print(estoque)

#Selecionando um valor específico pelo índice
print("\nQuantidade de notebooks em estoque: ")
print(estoque["Notebook"])

#Selecionando multiplos valores
print("\nQuantidade de notebooks e Camera em estoque: ")
print(estoque[["Notebook", "Camera"]].values)

#Filtrando produtos com estoque abaixo de 20
print("\nProdutos com estoque abaixo de 20 unidade: ")
print(estoque[estoque < 20])

#Operação Aritmética: aumentar estoque em 5 unidade
print("\nAumentando o estoque em 5 unidades para todos os produtos: ")
print(estoque + 5)

#Incluiindo um valor nulo para simular a falta de dados
estoque.loc["Headphone"] = None
print("\nEstoque com um valor nulo (Headphone): ")
print(estoque)

#Operações Aritméticas entre Séries
#Criando outra série com preços dos produtos
precos = pd.Series([3500,2500,1200,900,1500], index=produtos)

# Calculando o vlaor total do estoque (preço * quantidade)
print("\nValor total do estoque por produto (preço * quantidade): ")
print(precos * estoque)