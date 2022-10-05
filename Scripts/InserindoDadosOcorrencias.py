#acessando o arquivo vendedor.csv
import pandas as pd
from pyparsing import anyOpenTag #biblioteca de manipulação de dados

#variável para armazenar o endereço
#OBS: NA SUA CASA, VOCÊ PRECISA ALTERAR PAR AO ENDEREÇO DO SEU COMPUTADOR!!!
endereco = "C:\\Users\\claud\\OneDrive\\Claudio Bonel-DADOTECA\\_ProfessorClaudioBonel\\PUCRS\\Banco de dados relacional\\Dados\\Exercício\\"

#variáveis com o nome dos arquivos de dados
dp = pd.read_csv(endereco + "DP.csv",sep=",")
responsaveldp = pd.read_excel(endereco + "ResponsavelDP.xlsx")
municipio = pd.read_csv(endereco + "Municipio.csv",sep=",")
ocorrencias = pd.read_excel(endereco + "ocorrencias.xlsx")

#Coleta os dados dos arquivos para dentro do Python
tbDP = pd.DataFrame(dp)
tbResponsavelDP = pd.DataFrame(responsaveldp)
tbMunicipio = pd.DataFrame(municipio)
tbOcorrencias = pd.DataFrame(ocorrencias)

#Importa o sqlalchemy para conectar ao BD Vendas
import sqlalchemy as sa

#Criando a engrenagem de conexão com o BD
engine = sa.create_engine("sqlite:///BD//Ocorrencias.db")

#Criando um conexão variável de conexão com o BD
conn = engine.connect()

#Variável de definição de metadados, para identificar que estrutura será atualizada
metadata = sa.schema.MetaData(bind=engine)

#iniciando um sessão com o banco de dados
import sqlalchemy.orm as orm
Sessao = orm.sessionmaker(bind=engine) #Bind é um argumento que remete a vincular
sessao = Sessao()

#importando as classes que estão no arquivo ocorrencias.py para inserir dados
import ocorrencias as oc

#######################
# DP 
#######################
#Algoritmo para inserção de dados, utilziando o DataFrame tbDP
#Transforma os dados em uma lista, correlacionando os registros/linhas/tuplas, através do método dicionário (to_dict)
DadosDP = tbDP.to_dict(orient='records')

#Variável que representa a tabela que se deseja inserir os dados e, um metadados.
tabela_DP = sa.Table(oc.dp.__tablename__, metadata, autoload=True) #na classe que representa a tabela de ocorrências

#Inserindo dados a partir de uma conexão com a engrenagem de BD
try:
    conn.execute(tabela_DP.insert(), DadosDP)
    sessao.commit()
except ValueError:
    print(ValueError())

print("tbDP criada!")

#######################
# RESPONSÁVEL DP 
#######################
#Algoritmo para inserção de dados, utilziando o DataFrame tbResposavelDP
#Transforma os dados em uma lista, correlacionando os registros/linhas/tuplas, através do método dicionário (to_dict)
DadosRespoDP = tbResponsavelDP.to_dict(orient='records')

#Variável que representa a tabela que se deseja inserir os dados e, um metadados.
tabela_respDP = sa.Table(oc.responsaveldp.__tablename__, metadata, autoload=True) #na classe que representa a tabela de ocorrências

#Inserindo dados a partir de uma conexão com a engrenagem de BD
try:
    conn.execute(tabela_respDP.insert(), DadosRespoDP)
    sessao.commit()
except ValueError:
    print(ValueError())

print("tbResponsavelDP criada!")

#######################
# MUNICÍPIO 
#######################
#Algoritmo para inserção de dados, utilziando o DataFrame tbMunicipio
#Transforma os dados em uma lista, correlacionando os registros/linhas/tuplas, através do método dicionário (to_dict)
DadosMunicipio = tbMunicipio.to_dict(orient='records')

#Variável que representa a tabela que se deseja inserir os dados e, um metadados.
tabela_municipio = sa.Table(oc.municipio.__tablename__, metadata, autoload=True) #na classe que representa a tabela de ocorrências

#Inserindo dados a partir de uma conexão com a engrenagem de BD
try:
    conn.execute(tabela_municipio.insert(), DadosMunicipio)
    sessao.commit()
except ValueError:
    print(ValueError())

print("tbMunicipio criada!")

#######################
# OCORRÊNCIA 
#######################
#Algoritmo para inserção de dados, utilziando o DataFrame tbOcorrencias
#Transforma os dados em uma lista, correlacionando os registros/linhas/tuplas, através do método dicionário (to_dict)
DadosOcorrencias = tbOcorrencias.to_dict(orient='records')

#Variável que representa a tabela que se deseja inserir os dados e, um metadados.
tabela_ocorrencias = sa.Table(oc.ocorrencia.__tablename__, metadata, autoload=True) #na classe que representa a tabela de ocorrências

#Inserindo dados a partir de uma conexão com a engrenagem de BD
try:
    conn.execute(tabela_ocorrencias.insert(), DadosOcorrencias)
    sessao.commit()
except ValueError:
    print(ValueError())

print("tbOcorrencias criada!")

#Encerrando as sessões abertas
sessao.close_all()
print("Módulo de inserção de dados finalizado!")