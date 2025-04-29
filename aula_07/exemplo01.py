

def bah(texto):
    print(f"Olá {texto}")


def linha():
    print(30*"=")


linha()
print("Módulo 1")
linha()
print("Algoritmo")
linha()
print("Análise de Dados")
linha()
linha()
nome = input("Informe seu nome: ")
bah(nome)

def somar(a,b):
    s = a + b
    return s

for i in range(3):
    n1 = int(input("Informe um número: "))
    n2 = int(input("Informe outro número: "))

    soma = somar(n1,n2)
    print(soma)