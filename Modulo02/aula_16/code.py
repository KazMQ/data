# Instalação (se ainda não tiver instalado)
# pip install sqlalchemy pymysql pandas

from sqlalchemy import create_engine
import pandas as pd
import numpy as np

host = "localhost"
user = 'root'
password = ""
database = "bd_loja"

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

#obtendo dados
df_estoque = pd.read_sql("tb_produtos", engine)
#print(df_estoque.head())

df_estoque['TotalEstoque'] = df_estoque['qtd'] * df_estoque ['preco']
print(df_estoque[['produto', 'TotalEstoque']])
print(f'\nTotal Geral de produtos: R$ {df_estoque["TotalEstoque"].sum()}')

# NUMPY
array_estoque = np.array(df_estoque['TotalEstoque'])
#print(array_estoque)

#Calculando Medidas de Tendencia Central
media = np.mean(array_estoque)
mediana = np.median(array_estoque)
distancia = abs(media - mediana) / mediana

print('Medidas de Tendência Central')
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana}")
print(f'Distancia Média e Mediana: {distancia}')