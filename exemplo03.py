list_cadastro = []

def cadastro(num):
    for i in range(num):
        nome = input("Informe seu nome: ")
        valor = input("Informe o valor da venda: ")
        pessoa = {
        "Nome": nome,
        "Valor": valor
        }
        list_cadastro.append(pessoa)
cadastro

qtd = int(input("Quantas pessoas serão cadastradas: "))

cadastro(qtd)

print(list_cadastro)