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
    df_janeiro = pl.read_csv(data_path + '202501_NovoBolsaFamilia.csv', separator=';', encoding='iso-8859-1')


    print(df_janeiro.head())

    #Tempo final
    hora_final = datetime.now()
    result = hora_final - hora_inicio

    print(f"Tempo de execução: {result}")

except Exception as e:
    print(f'Erro ao obter dados {e}')