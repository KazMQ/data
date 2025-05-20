def cal():
    base = float(input("Quantos kilos foram pescados: "))
    if base > 100:
        excess = base - 100
        fine = excess*4
        print(f"Você pescou {excess} kilos a mais, gerando uma multa de {fine} reais")
    else:
        print("Sua pesca está dentro dos parâmetros")
cal()