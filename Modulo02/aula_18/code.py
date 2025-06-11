import pandas as pd
import numpy as np
from tabulate import tabulate


#Obtendo dados

try:
    print("Obtendo dados")
    Source = "https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv"
    df_ocorrencia = pd.read_csv(Source, sep=';', encoding='iso-8859-1')
    #print(df_ocorrencia.head())

    

    #Delimitando variaveis
    df_ocorrencia = df_ocorrencia[["munic", 'estelionato']]
    #Totalizando
    df_estelionato = df_ocorrencia.groupby('munic').sum(['estelionato'])
    #linkando municipios com casos
    Link = dict(zip(df_ocorrencia["munic"], df_ocorrencia['estelionato']))
   
    

except Exception as e:
    print(f"Erro de conexão: {e}")
    exit()

#Triagem dos dados

try:
    print("Obtendo informações sobre o padrão dos casos de estelionatos...")
    matriz_estelionato = np.array(df_estelionato['estelionato'])
    media_estelionato = np.mean(matriz_estelionato)
    mediana_estelionato = np.median(matriz_estelionato)
    delta_estelionato = abs((media_estelionato - mediana_estelionato)) / mediana_estelionato
    
    print('\nTabela de Estelionato por Município (Top 10):')
    print(tabulate(df_estelionato.sort_values(by="estelionato", ascending=False).head(10), headers='keys', tablefmt='grid'))

    print(f"MEDIDAS DE TENDENCIA CENTRAL")
    print(30*'=')
    print(f"Média dos estelionatos {media_estelionato:.2f}")
    print(f"Mediana dos estelionatos {mediana_estelionato:.2f}")
    print(f"Variação da média com a mediana: {delta_estelionato:.2f}")

    #MEDIDAS DE POSIÇÃO
    #Quartis
    q1 = np.quantile(matriz_estelionato, 0.25, method='weibull')
    q2 = np.quantile(matriz_estelionato, 0.5, method='weibull')
    q3 = np.quantile(matriz_estelionato, 0.75, method='weibull')

    #Treeshold para discrepancia
    iqr = q3 - q1

    #Variável de detecção
    limit_superior = q3 + (1.5 * iqr)
    limit_inferior = q1 - (1.5 * iqr)


#Detectando discrepancias
    
    df_estelionato_up = df_estelionato[df_estelionato['estelionato'] > limit_superior]
    df_estelionato_down = df_estelionato[df_estelionato['estelionato'] < limit_inferior]

#Detectando o big boi
    big = max(df_estelionato['estelionato'])
    max = df_ocorrencia['estelionato'].min()
    maxmunic = df_ocorrencia.loc[max, 'munic']
#Detectando o smoll boi
    smoll = min(df_estelionato['estelionato'])
    min = df_ocorrencia['estelionato'].max()
    minmunic = df_ocorrencia.loc[min, 'munic']

#Encerrando
    print("\nPrintando Outliers")
    print(45*'=')
    if len(df_estelionato_down) == 0:
        print("Não há outliers inferiores")
    else:
        print(tabulate(df_estelionato_down.sort_values(by="estelionato", ascending=True), headers='keys', tablefmt='grid'))
    print(45*'=')
    if len(df_estelionato_up) == 0:
        print("Não há outliers")
    else:
        print(tabulate(df_estelionato_up.sort_values(by="estelionato", ascending=False), headers='keys', tablefmt='grid'))

    print(f"O município com o maior número de casos é o {maxmunic}, apresentando um total de {big} casos")
    print(f"O município com o menor número de casos é o {minmunic}, apresentando um total de {smoll} casos")
except Exception as e:
    print(f"Erro de conexão: {e}")
    exit()
    
