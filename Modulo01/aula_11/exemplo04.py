import random

print("=== CAIXA ELETRÔNICO ===")

while True:
    try:
        saldo = 1000
        #saque = random.randint(0,1000)
        saque = float(input("Informe o valor do saque: "))
        print(f"Saque será de {saque}")
    
    except ValueError as e:
        print(f"Digite apenas número: {e}")

    else:
        if saque > 0:
            if saldo >= saque:
                 saldo -= saque
            elif saque > saldo:
                print("Saldo insuficiente")
        else:
                print("O saque precisa ser maior que 0")

    finally:
        print(f"Operação concluida! Seu saldo atual é de {saldo}")
