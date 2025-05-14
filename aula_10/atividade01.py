import random
import os

def somar(a,b):
    som = a + b
    print (som)
    return som

def sub(a,b):
    su = a - b
    print (su)
    return su

def div(a,b):
    di = a / b
    print (di)
    return di

def multi(a,b):
    mult = a * b
    print (mult)
    return mult



while True:
    numb1 = random.randint(1,10)
    numb2 = random.randint(1,10)
    #numb1 = int(input("Digite o primeiro número: "))
    #numb2 = int(input("Digite o segundo número: "))
    print(f"Qual operação deseja realizar? Os números de vez são {numb1} e {numb2}")
    chose = int(input("1 para soma, 2 para subtrair, 3 para dividir e 4 para multiplicar: "))
    if chose == 1:
        somar(numb1, numb2)
    elif chose == 2:
        sub(numb1,numb2)
    elif chose == 3:
        div(numb1, numb2)
    elif chose == 4:
        multi(numb1, numb2)
    else:
        print("Operação não identificada")
    

