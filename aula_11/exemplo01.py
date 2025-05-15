
try:
    n1 = float(input("Numero 1? "))
    n2 = float(input("Numero 2? "))
    div = n1 / n2
    print(div)

except ZeroDivisionError as e:
    print(f"Error, não pode dividir por 0 - {e}")

except ValueError as e:
    print(f"Não digite por extenso - {e}")