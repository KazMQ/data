def exemplo():
    try:
        n1 = float(input("Numero 1? "))
        n2 = float(input("Numero 2? "))
        div = n1 / n2
        print(div)

    except ZeroDivisionError as e:
        print(f"Error, não pode dividir por 0 - {e}")

    else: 
        print(div)

    finally:
        print("Tudo pronto!")


def exem():
    try:
        n1 = float(input("Numero 1? "))
        n2 = float(input("Numero 2? "))
        div = n1 / n2
        print(div)

    except Exception as e:
        print(f"Error, não pode dividir por 0 - {e}")

    else: 
        print(div)

    finally:
        print("Tudo pronto!")


