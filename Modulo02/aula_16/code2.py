# Instalação (se ainda não tiver instalado)
# pip install sqlalchemy pymysql pandas

from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import os

load_dotenv()

host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv("DB_PASS")
database = os.getenv("DB_DATABASE")

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

query = "SELECT * FROM tb_vendas WHERE nome_vendedor = 'Carlos Silva'"
#obtendo dados
df_estoque = pd.read_sql(query, engine)
#print(df_estoque.head())

df_estoque['Vendas'] = df_estoque['qtd'] * df_estoque ['preco']
#print(df_estoque[['produto', 'Vendas']])
print(f'\nTotal, vendemos R$ {df_estoque["Vendas"].sum():.2f} em produtos')

# NUMPY
array_estoque = np.array(df_estoque['Vendas'])
#print(array_estoque)

media = np.mean(array_estoque)
mediana = np.median(array_estoque)
distancia = abs(media - mediana) / mediana

#Coluna da comissão dos vendedores
df_estoque['comissao'] = (df_estoque['Vendas']*0.09).round(2)
print(df_estoque[['nome_vendedor','Vendas', 'comissao']])

print(f"Em média, estamos vendendo R$ {media:.2f} por produto")

if distancia < 1:
    print(f"Visto que a varianação entre média e mediana é de {distancia} e menor que 1, podemos dizer que a média é confiavel")
elif distancia >= 1:
    print(f"Visto que a variação entre a média e mediana é de {distancia} e maior do que 1, há muita variação entre os termos, logo a média não é uma boa métrica")


