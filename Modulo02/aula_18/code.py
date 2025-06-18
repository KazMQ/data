import pandas as pd
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt


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
    df_estelionato = df_ocorrencia.groupby('munic').sum(['estelionato']).reset_index()
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

    #Amplitude
    maximo = np.max(matriz_estelionato)
    minimo = np.min(matriz_estelionato)
    amplitude_total = maximo - minimo


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
#Variancia é a média dos quadrados das diferenças entre cada valor e a média 
    variancia = np.var(matriz_estelionato)
    
    #Distancia entre média e variancia
    distancia_var_media = variancia / (media_estelionato ** 2)

    #Desvio Padrão
    #É a raiz da
    #O quanto os dados podem estár se distancia da média
    desvio_padrao = np.std(matriz_estelionato)

    #Coeficiente de variação é a magnitude do desvio padrão
    coef_variacao = desvio_padrao / media_estelionato

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

    print(f'Limite Inferior: {limit_inferior}')
    print(f'Mínimo: {minimo}')
    print(f'1º Quartil: {q1}')
    print(f'2º Quartil: {q2}')
    print(f'3º Quartil: {q3}')
    print(f'IQR: {iqr}')
    print(f'Máximo: {maximo}')
    print(f'Limite Superior: {limit_superior}')
    

    print('\nOUTRAS AS MEDIDAS: ')
    print(30*'-')
    print(f'Amplitude Total: {amplitude_total}')
    print(f'Média: {media_estelionato:.3f}')
    print(f'Mediana: {mediana_estelionato}')
    print(f'Distância Média e Mediana: {delta_estelionato:.4f}')
    print(f"Desvio Padrão: {desvio_padrao:.2f}")
    print(f"Coeficiente de variação: {coef_variacao:.2f}")

    # PLOTANDO GRÁFICO
# Matplotlib

    # import matplotlib.pyplot as plt
    # fig, ax = plt.subplots(figsize=(10, 6))
    # ax.boxplot(array_roubo_veiculo, vert=False, showmeans=True)
    
    plt.subplots(2, 2, figsize=(16, 10))
    plt.suptitle('Análise de Estelionatos no RJ') 

    # POSIÇÃO 01
    # BOXPLOT
    plt.subplot(2, 2, 1)  
    plt.boxplot(matriz_estelionato, vert=False, showmeans=True)
    plt.title("Boxplot dos Dados")

    # POSIÇÃO 02
    # MEDIDAS
    # Exibição de informações estatísticas
    plt.subplot(2, 2, 2)
    plt.title('Medidas Estatísticas')
    plt.text(0.1, 0.9, f'Limite inferior: {limit_inferior}', fontsize=10)
    plt.text(0.1, 0.8, f'Menor valor: {minimo}', fontsize=10) 
    plt.text(0.1, 0.7, f'Q1: {q1}', fontsize=10)
    plt.text(0.1, 0.6, f'Mediana: {mediana_estelionato}', fontsize=10)
    plt.text(0.1, 0.5, f'Q3: {q3}', fontsize=10)
    plt.text(0.1, 0.4, f'Média: {media_estelionato:.3f}', fontsize=10)
    plt.text(0.1, 0.3, f'Maior valor: {maximo}', fontsize=10)
    plt.text(0.1, 0.2, f'Limite superior: {limit_superior}', fontsize=10)

    plt.text(0.5, 0.9, f'Distância Média e Mediana: {delta_estelionato:.4f}', fontsize=10)
    plt.text(0.5, 0.8, f'IQR: {iqr}', fontsize=10)
    plt.text(0.5, 0.7, f'Amplitude Total: {amplitude_total}', fontsize=10)
    
    # POSIÇÃO 03
    # OUTLIERS INFERIORES
    plt.subplot(2, 2, 3)
    plt.title('Outliers Inferiores')
    # Se o DataFrame do outliers não estiver vazio
    if not df_estelionato_down.empty:
        dados_inferiores = df_estelionato_down.sort_values(by='estelionato', ascending=True) #crescente
        # Gráfico de Barras
        plt.barh(dados_inferiores['munic'], dados_inferiores['estelionato'])
    else:
        # Se não houver outliers
        plt.text(0.5, 0.5, 'Sem Outliers Inferiores', ha='center', va='center', fontsize=12)
        plt.title('Outilers Inferiores')
        plt.xticks([])
        plt.yticks([])
    # POSIÇÃO 04
    # OUTLIERS SUPERIORES
    plt.subplot(2, 2, 4)
    plt.title('Outliers Superiores')
    if not df_estelionato_up.empty:
        dados_superiores = df_estelionato_up.sort_values(by='estelionato', ascending=True)

        # Cria o gráfico e guarda as barras
        barras = plt.barh(dados_superiores['munic'], dados_superiores['estelionato'], color='black')
        # Adiciona rótulos nas barras
        plt.bar_label(barras, fmt='%.0f', label_type='edge', fontsize=8, padding=2)

        # Diminui o tamanho da fonte dos eixos
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)

        plt.title('Outliers Superiores')
        plt.xlabel('Total Estlionato')    
    else:
        # Se não houver outliers superiores, exibe uma mensagem no lugar.
        plt.text(0.5, 0.5, 'Sem outliers superiores', ha='center', va='center', fontsize=12)
        plt.title('Outliers Superiores')
        plt.xticks([])
        plt.yticks([])

    # Ajusta os espaços do layout para que os gráficos não fiquem espremidos
    plt.tight_layout()
    # Mostra a figura com os dois gráficos
    plt.show()
except Exception as e:
    print(f"Erro de conexão: {e}")
    exit()
    
print(f"PARECER FINAL")   
print(30*'=')
print(f"O município com o maior número de casos é o {maxmunic}, apresentando um total de {big} casos")
print(f"O município com o menor número de casos é o {minmunic}, apresentando um total de {smoll} casos")
if delta_estelionato > 1:
    print(f"A variação entre a média e mediana é de {delta_estelionato:.2f}, o que torna a média não confiável")
    print(f"Isso implica a existência de outliers maiores dentro do banco de dados")
