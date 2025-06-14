
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from utils import limpar_nome_municipio



try:
    print("Obtendo dados")
    Source = "https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv"
    df_ocorrencia = pd.read_csv(Source, sep=';', encoding='iso-8859-1')
    #print(df_ocorrencia.head())

    #for i in range(2):
    #   df_ocorrencia["munic"] = df_ocorrencia['munic'].apply(limpar_nome_municipio)

    #Delimitando variaveis
    df_ocorrencia = df_ocorrencia[["munic", 'roubo_veiculo']]
    #Totalizando
    df_roubo_veiculo = df_ocorrencia.groupby('munic').sum(['roubo_veiculo'])
    df_roubo_veiculo = df_ocorrencia.groupby('munic').sum(['roubo_veiculo']).reset_index()
   
    #print(df_roubo_veiculo.to_string())

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

    # print(f"MEDIDAS DE TENDENCIA CENTRAL")
    # print(30*'=')
    # print(f"Média dos roubos {media_roubo_veiculo:.2f}")
    # print(f"Mediana dos roubos {mediana_roubo_veiculo:.2f}")
    # print(f"Distancia entre as medias e mediana {distancia_roubo_veiculo:.2f}")

    #MEDIDAS DE POSIÇÃO
    #Quartis
    q1 = np.quantile(array_roubo_veiculo, 0.25, method='weibull')
    q2 = np.quantile(array_roubo_veiculo, 0.5, method='weibull')
    q3 = np.quantile(array_roubo_veiculo, 0.75, method='weibull')

    #Medidas de Dispersão
    #print("\nMedidas de Dispersão")
    max = np.max(array_roubo_veiculo)
    min = np.min(array_roubo_veiculo)
    delta = max - min  

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

    print("\nMedidas")
    print(30*"=")
    print(f"Limite superior: {limit_inferior}")
    print(f"Menor valor: {min}")
    print(f"\nMEDIDAS POSIÇÃO")
    print(30*'=')
    print(f"Q1: {q1}")
    print(f"Q2: {q2}")
    print(f"Q3: {q3}")
    print(f"Maior valor: {max}")
    print(f"Limite inferior: {limit_superior}")
    print(f"Média: {media_roubo_veiculo}")
    print(f"Mediana: {mediana_roubo_veiculo}")
    print(f"Distância média/mediana: {delta}")
    
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

df_roubo_veiculo = df_ocorrencia.groupby('munic').sum(['roubo_veiculo']).reset_index()
# pip install matplotlib

try:
    # Cria uma figura com 1 linha e 2 colunas de subgráficos (side by side)
    # figsize define o tamanho da figura total
    fig, ax = plt.subplots(1, 2, figsize=(18, 6))
    

    # OUTLIERS INFERIORES
    # Verifica se existem outliers inferiores
    if not df_roubo_veiculo_outliers_inferiores.empty:
        print("Queijo")
        # Ordena os dados de forma crescente pelo número de roubos
        dados_inferiores = df_roubo_veiculo.sort_values(by='roubo_veiculo', ascending=True)
        
        # Cria gráfico de barras horizontais com os municípios e seus valores
        ax[0].barh(dados_inferiores['munic'], dados_inferiores['roubo_veiculo'])
    
    else:
        print("Presunto")
        # Caso não haja outliers inferiores, exibe os 10 municípios que obtiveram menos roubos (bootom 10)
        dados_inferiores = df_roubo_veiculo_menores.sort_values(by='roubo_veiculo', ascending=True).head(10)

        # ax[0].text(0.5, 0.5, 'Sem Outliers Inferiores', ha='center', va='center', fontsize=12)
        barras = ax[0].bar(dados_inferiores['munic'], dados_inferiores['roubo_veiculo'], color='black')
        ax[0].bar_label(barras, label_type='edge', padding=3, fontsize=8)
        ax[0].tick_params(axis='x', rotation=75, labelsize=8)
        # Define o título do subplot
        ax[0].set_title('Menores Roubos')
        # Remove os marcadores dos eixos x e y
        ax[0].set_xticks([])
        ax[0].set_yticks([])

        # ##### VISUAL ######
        # Rótulo no final das barras e com tam 8
        # barras = ax[0].bar(dados_inferiores['munic'], dados_inferiores['roubo_veiculo'], color='green')
        # ax[0].bar_label(barras, label_type='edge', padding=3, fontsize=8)
        # # rotaciona o eixo x para melhorar a visualização
        # ax[0].tick_params(axis='x', rotation=75, labelsize=8)
 
    # OUTLIERS SUPERIORES
    # Verifica se existem outliers superiores
    if not df_roubo_veiculo_outliers_maiores.empty:
        # Ordena os dados de forma crescente
        dados_superiores = df_roubo_veiculo_outliers_maiores.sort_values(by='roubo_veiculo', ascending=True)

        # Cria o gráfico de barras horizontais com os municípios e seus valores
        ax[1].barh(dados_superiores['munic'], dados_superiores['roubo_veiculo'], color='black')
        # Define o título e o rótulo do eixo x
        ax[1].set_title('Outliers Superiores')
        ax[1].set_xlabel('Total Roubos de Veículos')

        # ###### "VISUAL" #####
        # Rótulo de dados 0 casas decimais, edge "final da barra", tamanho 8 a 1 padding "distância"
        barras = ax[1].barh(dados_superiores['munic'], dados_superiores['roubo_veiculo'], color='black')
        ax[1].bar_label(barras, fmt='%.0f', label_type='edge', fontsize=8, padding=1)  
        # Tamanho do conteúdo do eixo Vertical "Y"
        ax[1].tick_params(axis='y', labelsize=8)

    else:
        # Caso não haja outliers superiores, exibe uma mensagem centralizada
        ax[1].text(0.5, 0.5, 'Sem outliers superiores', ha='center', va='center', fontsize=12)

        # Define o título do subplot
        ax[1].set_title('Outliers Superiores')

        # Remove os marcadores dos eixos x e y
        ax[1].set_xticks([])
        ax[1].set_yticks([])

    # Ajusta automaticamente os elementos do layout para não se sobreporem
    plt.tight_layout()

    # Exibe os gráficos
    plt.show()

except Exception as e:
    print(f'Erro ao plotar {e}')

