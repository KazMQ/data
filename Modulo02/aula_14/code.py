#pip install sqlalchemy pymysql
from sqlalchemy import create_engine, text

#variáveis de conexão
host = 'localhost'
user = 'root'
password = ''
database = 'bd_analise'

#Função para fazer a conexão com o banco de dados
def conecta_bd():
    try:
        #URL de conexão com o banco
        engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")

        with engine.connect() as conexao:
            query = "Select * FROM vendas2" #Consulta no banco de dados

            result = conexao.execute(text(query))
           
            if result.rowcount > 0:
                for item in result:
                    #print(item) #Imprime todas as colunas
                    print(item[0], item[1], item [2])
    except Exception as e:
        print(f"Algo deu errado: {e}")

conecta_bd()