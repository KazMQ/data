
import pandas as pd 
import numpy as np 
from utils import limpar_nome_municipio



try:
    print("Obtendo dados")
    Source = "https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv"
    df_ocorrencia = pd.read_csv(Source, sep=';', encoding='iso-8859-1')
    #print(df_ocorrencia.head())

    for i in range(2):
        df_ocorrencia["munic"] = df_ocorrencia['munic'].apply(limpar_nome_municipio)

    #Delimitando variaveis
    df_ocorrencia = df_ocorrencia[["munic", 'roubo_veiculo']]
    #Totalizando
    df_roubo_veiculo = df_ocorrencia.groupby('munic').sum(['roubo_veiculo'])
    
   
    print(df_roubo_veiculo.to_string())

except Exception as e:
    print(f"Erro de conexão: {e}")
    exit()

#Iniciando análise
    
try: 
    print("Obtendo informações sobre padrão de roubos de veiculos...")
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])
    media_roubo_veiculo = np.mean(array_roubo_veiculo)
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)
    distancia_roubo_veiculo = abs((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo)

    print(f"MEDIDAS DE TENDENCIA CENTRAL")
    print(30*'=')
    print(f"Média dos roubos {media_roubo_veiculo:.2f}")
    print(f"Mediana dos roubos {mediana_roubo_veiculo:.2f}")
    print(f"Distancia entre as medias e mediana {distancia_roubo_veiculo:.2f}")

    #MEDIDAS DE POSIÇÃO
    #Quartis
    q1 = np.quantile(array_roubo_veiculo, 0.25, method='weibull')
    q2 = np.quantile(array_roubo_veiculo, 0.5, method='weibull')
    q3 = np.quantile(array_roubo_veiculo, 0.75, method='weibull')

    print(f"MEDIDAS POSIÇÃO")
    print(30*'=')
    print(f"Q1: {q1}")
    print(f"Q2: {q2}")
    print(f"Q3: {q3}")

    #Roubam mais e Roubam menos

    df_roubo_veiculo_menores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < q1]
    df_roubo_veiculo_maiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > q3]

    print("\nMunicipios com números baixos de roubo")
    print(30*"=")
    print(df_roubo_veiculo_menores.sort_values(by='roubo_veiculo', ascending=True))

    print("\nMunicipios com números altos de roubo")
    print(30*"=")
    print(df_roubo_veiculo_maiores.sort_values(by='roubo_veiculo', ascending=False))

    iqr = q3 - q1

    limit_superior = q3 + (1.5 * iqr)
    limit_inferior = q1 - (1.5 * iqr)

    print("\nLimites - Medidas de posição")
    print(30*"=")
    print(f"Limite inferior: {limit_inferior}")
    print(f"Limite superior: {limit_superior}")

    df_roubo_veiculo_outliers_maiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > limit_superior]
    df_roubo_veiculo_outliers_inferiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < limit_inferior]

    print("\nPrintando Outliers")
    print(45*'=')
    if len(df_roubo_veiculo_outliers_inferiores) == 0:
        print("Não há outliers inferiores")
    else:
        print(df_roubo_veiculo_outliers_inferiores.sort_values(by="roubo_veiculo", ascending=True))
    if len(df_roubo_veiculo_outliers_maiores) == 0:
        print("Não há outliers")
    else:
        
        print(df_roubo_veiculo_outliers_maiores.sort_values(by="roubo_veiculo", ascending=False))

except Exception as e:
    print(F"ERRO {e}")