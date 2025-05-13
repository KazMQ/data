list_cadastro = []

def cadastro(num):
    for i in range(num):
        nome = input("Informe seu nome: ")
        valor = float(input("Informe o valor da venda: "))
        pessoa = {
        "Nome": nome,
        "Valor": valor
        }
        list_cadastro.append(pessoa)

def mediat():
    tot = 0
    for pessoa in list_cadastro:
        tot += pessoa["Valor"]
    med = tot / len(list_cadastro)
    return tot, med
    
def search_big():
    big = 0
    vendedor = ""
    for v in list_cadastro:
        if v["Valor"] > big:
            big = v["Valor"]
            vendedor = v["Nome"]
    return big, vendedor

def buscar_vendedor(nome):
    resp = ""
    v1 = 0
    for cadastro in list_cadastro:
        if cadastro["Nome"] == nome:
            resp = cadastro["Nome"]
            v1 = cadastro["Valor"]
            return resp, v1
        return resp, v1


qtd = int(input("Quantas pessoas serão cadastradas: "))

cadastro(qtd)

print(list_cadastro)

buscar_vendedor()

total, media = mediat()

vendedor, big = search_big()

print(f"Total é {total} e a média é {media}")
print(f"A maior venda foi do {vendedor} com sua venda de {big}")