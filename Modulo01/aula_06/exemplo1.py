qtd_produtos = int(input("Quantos produtos: "))
contador = 1

while contador <= 5:
    nome_produto = input("Informe o nome: ")
    print(nome_produto)
    contador = contador + 1

    c = 6
    s = 0
    while c > 0:
        n = float(input("Informe número: "))
        s = s + n
        c -= 1
    print(f"A some é {s}")

    