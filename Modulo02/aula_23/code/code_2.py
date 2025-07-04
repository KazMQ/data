import pandas as pd
from datetime import datetime
import polars as pl 
#Obtendo dados

try:
    data_path = r'./dados/'
    hora_inicio = datetime.now()
    print("Carregando")

    #Pandas
    #df_janeiro = pd.read_csv(data_path + '202501_NovoBolsaFamilia.csv', sep=';', encoding='iso-8859-1')
    
    #Polars
    #df_janeiro = pl.read_csv(data_path + '202502_NovoBolsaFamilia.csv', separator=';', encoding='iso-8859-1')
    lista = ['202502_NovoBolsaFamilia.csv', 
             '202501_NovoBolsaFamilia.csv',
             '202503_NovoBolsaFamilia.csv',
             '202504_NovoBolsaFamilia.csv', 
             '202505_NovoBolsaFamilia.csv']

    df_bolsa = None
    
    for arquivo in lista:
        print(f"Processando o arquivo {arquivo}")
        df = pl.read_csv(data_path + arquivo, separator=';', encoding='iso-8859-1')
        #df = pd.read_csv(data_path + arquivo, sep=';', encoding='iso-8859-1')

        if df_bolsa is None:
            df_bolsa = df
        else:
            df_bolsa = pl.concat([df_bolsa, df])
            print(df)
            print(df.shape)
            del df

    print('Bolsa Familia Concatenado')
    print(df_bolsa.head())
    print(df_bolsa.shape)
    

    #Tempo final
    hora_final = datetime.now()
    result = hora_final - hora_inicio

    print(f"Tempo de execução: {result}")

except Exception as e:
    print(f'Erro ao obter dados {e}')