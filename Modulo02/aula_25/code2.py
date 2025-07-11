import pandas as pd 
import polars as pl 
from datetime import datetime
import pyarrow.parquet as pq
import numpy as np 

#Lembrar de usar pip install fastparquet para rodar melhor


data_path_bronze = r'bronze/'

try:

    print("Inciando a leitura do arquivo Parquet...")
    inicio = datetime.now()
    #PANDAS
    #df_bolsa_familia = pd.read_parquet(data_path_bronze + 'bolsa_familia.parquet')
    
    #POLARS
    #Scan Parquet gera um plano de execução
    df_bolsa_familia = pl.scan_parquet(data_path_bronze + 'bolsa_familia.parquet')
    df_bolsa_familia = df_bolsa_familia.collect()
    
    print(df_bolsa_familia.head())

    final = datetime.now()
    print(f'Tempo de execução: {final - inicio}')
    print('Arquivo lido com sucesso')

except Exception as e:
    print(f"Erro ao obter dados: {e}")


try:
    array_valor_parcela = np.array(df_bolsa_familia['VALOR PARCELA'])
    media = np.mean(array_valor_parcela)
    mediana = np.median(array_valor_parcela)
    distancia = abs(media - mediana) / mediana


    print(array_valor_parcela)
    print(media)
    print(mediana)
    print(distancia)
except Exception as e:
    print(f"Erro ao obter dados: {e}")
    