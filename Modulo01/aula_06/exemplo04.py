climas = ["Ensolarado", "Nublado", "Chuvoso", "Tempestade", "Ensolarado"]
climas_unicos = list(set(climas))
while True:
    climas = input(f"Digite a previsão do tempo de hoje dentre as opções a seguir {climas_unicos}: ")
    for clima in climas:
        if climas == "Ensolarado":
            print("Aproveite o dia!")
            break
        else:
            print ("Leve o guarda chuva")
            break
