import pandas as pd 
import polars as pl 
from datetime import datetime
import pyarrow.parquet as pq
import numpy as np 
import matplotlib.pyplot as plt

#Lembrar de usar pip install fastparquet para rodar melhor


data_path_bronze = r'bronze/'

try:

    print("Inciando a leitura do arquivo Parquet...")
    inicio = datetime.now()
    
    #POLARS
    #Scan Parquet gera um plano de execução
    df_bolsa_familia = (pl.scan_parquet(data_path_bronze + 'bolsa_familia.parquet')
                        .select(pl.col(['NOME MUNICÍPIO','VALOR PARCELA']))
                        .filter(pl.col("VALOR PARCELA")> 1518)
                        )


    df_bolsa_familia = df_bolsa_familia.collect()
    
    print(df_bolsa_familia.head())

    final = datetime.now()
    print(f'Tempo de execução: {final - inicio}')
    print('Arquivo lido com sucesso')

except Exception as e:
    print(f"Erro ao obter dados: {e}")


try:
    array_valor_parcela = np.array(df_bolsa_familia['VALOR PARCELA'])
    
except Exception as e:
    print(f"Erro ao obter dados: {e}")


#Visualizando a distribuição
try:
    print("Visualizando a distribuição")

    #Criar boxplot
    plt.boxplot(array_valor_parcela, showmeans=True,vert=False)
    plt.title("Distribuição das parcelas")
    plt.show()

except Exception as e:
    print(f"Erro ao obter dados: {e}")
