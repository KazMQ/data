dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
prevs = ["Nublado", "Chuvoso", "Tempestade", "Ensolarado", "Ensolarado"]
check = list(zip(dias, prevs))

while True:
    for i, prev in enumerate(prevs):
        if prev == "Ensolarado":
            print(f"{dias[i]} vai ser bom ja que a previsão é {prevs[i]}! Aproveite o dia!")
            
        else:
            print (f"{dias[i]} vai dar ruim com a previsão de {prevs[i]}! Fica em casa amigão")
    break