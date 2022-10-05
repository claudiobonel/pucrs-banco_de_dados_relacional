#acessando o arquivo vendedor.csv
import pandas as pd #biblioteca de manipulação de dados

#variável para armazenar o endereço
#OBS: NA SUA CASA, VOCÊ PRECISA ALTERAR PAR AO ENDEREÇO DO SEU COMPUTADOR!!!
endereco = "C:\\Users\\claud\\OneDrive\\Claudio Bonel-DADOTECA\\_ProfessorClaudioBonel\\PUCRS\\Banco de dados relacional\\Dados\\Exemplo\\"

#variavel com o nome do arquivo
vendedor = pd.read_csv(endereco + "vendedor.csv",sep=";")

#Coleta os dados do arquivo para dentro do Python
tbVendedor = pd.DataFrame(vendedor)
#print(tbVendedor)

#Importa o sqlalchemy para conectar ao BD Vendas
import sqlalchemy as sa
#Criando a engrenagem de conexão com o BD
engine = sa.create_engine("sqlite:///BD//Vendas.db")

#iniciando um sessão com o banco de dados
import sqlalchemy.orm as orm
Sessao = orm.sessionmaker(bind=engine) #Bind é um argumento que remete a vincular
sessao = Sessao()

#importando as classes que estão no arquivo vendas.py para inserir dados
import vendas as vd

#######################
# VENDEDOR
#######################
#Algoritmo para inserção de dados, utilziando o DataFrame tbVendedor
for i in range(len(tbVendedor)):
    dado_vendedor = vd.vendedor(
                                registro_vendedor = int(tbVendedor["registro_vendedor"][i]),
                                cpf = tbVendedor["cpf"][i],
                                nome = tbVendedor["nome"][i],
                                genero = tbVendedor["genero"][i],
                                email = tbVendedor["email"][i]
                            )
    try:
        sessao.add(dado_vendedor)
        sessao.commit()
    except ValueError:
        print(ValueError())

print ("tbVendedor criada!")

#Algoritmo para inserção de dados, utilziando o DataFrame tbProduto

#variavel com o nome do arquivo
produto = pd.read_excel(endereco + "produto.xlsx")

#Coleta os dados do arquivo para dentro do Python
tbProduto = pd.DataFrame(produto)

#######################
# PRODUTO
#######################
#Criando um conexão variável de conexão com o BD
conn = engine.connect()

#Variável de definição de metadados, para identificar que estrutura será atualizada
metadata = sa.schema.MetaData(bind=engine)

#Algoritmo para inserção de dados, utilziando o DataFrame tbProduto
#Transforma os dados em uma lista, correlacionando os registros/linhas/tuplas, através do método dicionário (to_dict)
DadosProduto = tbProduto.to_dict(orient='records')

#Variável que representa a tabela que se deseja inserir os dados e, um metadados.
tabela_produto = sa.Table(vd.produto.__tablename__, metadata, autoload=True) #na classe que representa a tabela de ocorrências

#Inserindo dados a partir de uma conexão com a engrenagem de BD
try:
    conn.execute(tabela_produto.insert(), DadosProduto)
    sessao.commit()
except ValueError:
    print(ValueError())

print("tbProduto criada!")

sessao.close_all()
print("Módulo de inserção de dados finalizado!")