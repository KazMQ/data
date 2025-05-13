import random
import os

os.system("cls")
# n = random.randint(1,5)
# m = random.randint(1,5)

# print (n, m)

# lst = [random.randint(1,10) for i in range (5)]
# print (lst)

#Exemplo 2

def gerar_numb (i,f,q):
    lst_numb = [random.randint(i,f) for num in range(q)]
    return lst_numb

ini = int(input("Informe o primeiro número: "))
fin = int(input("Informe o último número: "))
qtd = int(input("Quantos números?: "))

numeros = gerar_numb(ini, fin, qtd)
print(numeros)