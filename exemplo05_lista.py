dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
prevs = ["Nublado", "Chuvoso", "Tempestade", "Ensolarado", "Ensolarado"]
check = list(zip(dias, prevs))

while True:
    for i, prev in enumerate(prevs):
        if prev == "Ensolarado":
            print(f"{dias[i]} vai ser bom! Aproveite o dia!")
            
        else:
            print (f"{dias[i]} vai dar ruim! Fica em casa amigão")
    break