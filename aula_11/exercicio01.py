while True:
    try:
        numb1 = float(input("Digite a primeira nota: "))
        numb2 = float(input("Digite a segunda nota: "))
        media = (numb1 + numb2)/2
    except ValueError as e:
        print("Use apenas números!")
    
    else:
        if media >= 6 and media <= 10:
            print(f"Aluno aprovado com média de {media}!")
        elif media < 6 and media >= 4:
            print(f"Aluno de recuperação devido a média {media}")
        elif media < 4 and media >= 0:
            print (f"Aluno está reprovado devido a média de {media}")
        else:
            print("Valor inválido inserido!")
    finally:
        print("FIM DO PROGRAMA! Reinciando...")