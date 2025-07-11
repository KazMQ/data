import pandas as pd 
import polars as pl 
from datetime import datetime
import pyarrow.parquet as pq

#Lembrar de usar pip install fastparquet para rodar melhor


data_path_bronze = r'bronze/'

try:

    print("Inciando a leitura do arquivo Parquet...")
    inicio = datetime.now()
    #PANDAS
    #df_bolsa_familia = pd.read_parquet(data_path_bronze + 'bolsa_familia.parquet')
    
    #POLARS
    df_bolsa_familia = pl.read_parquet(data_path_bronze + 'bolsa_familia.parquet')
    print(df_bolsa_familia.head())

    print(df_bolsa_familia.columns) #Mostras as colunas
    print(df_bolsa_familia.dtypes) #Tipos de dados

    final = datetime.now()
    print(f'Tempo de execução: {final - inicio}')
    print('Arquivo lido com sucesso')

except Exception as e:
    print(f"Erro ao obter dados: {e}")


    