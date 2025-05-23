import pandas as pd

data = {
    "Nome": ["Ana", "Joao", "Maria"],
    "Idade" : [23, 25 , 29],
    "Genero": ["F", "M", "F"],
    "Altura" : [1.70, 1.80, 1.75]
}

df_dados = pd.DataFrame(data)
print(df_dados)

print("\nVariáveis Quantitativas")
print(30*"=")

#IDADE
print("Exibindo idade: ")
print(df_dados["Idade"])

#Altura

print("Exibindo altura: ")
print(df_dados["Altura"])

#Nome
print("Exibindo nomes: ")
print(df_dados["Nome"])

#Genero
print("Exibindo generos: ")
print(df_dados["Genero"])



