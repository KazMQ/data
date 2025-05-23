import numpy as np

vendas = np.array([150,180,200,220,250,280,300,320,400,1500])

media = np.mean(vendas)
print("Média: R$", media*1000)

mediana = np.median(vendas)
print("Mediana: R$", mediana*1000)

print("Analisando os dados passados, nota-se que há um que foge da progressão padrão dos outros. Observe:")

q1 = np.quantile(vendas, 0.25)
q2 = np.quantile(vendas, 0.50)
q3 = np.quantile(vendas, 0.75)
q4 = np.quantile(vendas, 1)
print(f"Q1 representa os menores valores, e sua média é {q1}\nJá Q2 possui os números com até metade do valor máximo, e sua média é {q2}\nAgora, temos os maiores no {q3}.\nEm enfim temos {q4}. Agora fica claro que o melhor representante do valor típico é a mediana")
