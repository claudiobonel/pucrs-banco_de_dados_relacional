#Primeira coisa a se fazer é importar o SQLAlchemy para utilizar os métodos no Python
import sqlalchemy as sa 

#Agora, vamos criar uma engrenagem com o Banco de dados.
#Para nossa disciplina, utilizaremos o SQLite
engine = sa.create_engine("sqlite:///BD//Vendas.db")

#Uma vez com a engrenagem de banco conectada, precisamos de importar
#um dos principais métodos do SQLAlchemy, que é a declarative_base()

#Esse método é, literalmente, a BASE para a realização do Mapeamento
#dos objetos no SQLite. É ele que vai te possibilitar a criação de uma classe
#para, consequente, criação das tabelas e colunas.
import sqlalchemy.orm as orm
base = orm.declarative_base() #variável de ORM

#criando tbCliente, via ORM
class cliente(base):
    #Definição do nome da tabela (entidade). 
    #NECESSARIAMENTE essa variável precisa ser __tablename__
    #É OBRIGATÓRIO para a classe que existe uma __tablename__
    __tablename__ = 'tbCliente'

    #definição das colunas (atributos)
    #Chaves primárias com tipo de dados TEXTO e a integridade é da entidade, o BD automaticamente
    #criará um index COLLATE BINARY, para diferenciam maiúsculas de minúsculas
    #comparando bytes diretamente, de forma a garantir que NÃO haja repetições
    cpf = sa.Column(sa.CHAR(14), primary_key = True,index=True) #Teremos 2 índices criados.
    nmCliente = sa.Column(sa.VARCHAR(100), nullable = False)
    email = sa.Column(sa.VARCHAR(50), nullable = False)
    faixa_salarial = sa.Column(sa.DECIMAL(10,2))
    dia_mes_aniversario = sa.Column(sa.CHAR(5))
    genero = sa.Column(sa.CHAR(1))
    bairro = sa.Column(sa.VARCHAR(50))
    cidade = sa.Column(sa.VARCHAR(50))
    uf = sa.Column(sa.CHAR(2))

#crindo tbFornecedor, via ORM 
#É necessário criar antes, pois a tbProduto tem uma coluna de chave estrangeira, 
#onde a tbFornecedor é a tabela estrangeira
class fornecedor(base):
    __tablename__ = 'tbFornecedor'

    registro = sa.Column(sa.INTEGER, primary_key = True, index=True)
    nome_fantasia = sa.Column(sa.VARCHAR(100), nullable = False)
    razao_social = sa.Column(sa.VARCHAR(100), nullable = False)
    cidade = sa.Column(sa.VARCHAR(50))
    uf = sa.Column(sa.CHAR(2))

#criando tbProduto, via ORM
class produto(base):
    __tablename__ = 'tbProduto'

    codBarras = sa.Column(sa.INTEGER, primary_key = True, index=True)
    registro = sa.Column(sa.INTEGER, sa.ForeignKey('tbFornecedor.registro', ondelete='NO ACTION', onupdate='CASCADE'))
    dscProduto = sa.Column(sa.VARCHAR(100), nullable = False)
    genero = sa.Column(sa.CHAR(1))  

#Criando a tbVendedor, via ORM
class vendedor(base):
    __tablename__ = 'tbVendedor'

    registro_vendedor = sa.Column(sa.INTEGER, primary_key = True, index=True)
    cpf = sa.Column(sa.CHAR(14), nullable = False)
    nome = sa.Column(sa.VARCHAR(100), nullable = False)
    genero = sa.Column(sa.CHAR(1))  
    email = sa.Column(sa.VARCHAR(50))

#criar a tbVendas, via ORM
class vendas(base):
    __tablename__ = 'tbVendas'

    idTransacao = sa.Column(sa.INTEGER, primary_key=True, index=True)
    #Em chaves estrangeiras, pelo fato de permitir a repetição. NÃO será criado o COLLATE BINARY.
    cpf = sa.Column(sa.CHAR(14), sa.ForeignKey('tbCliente.cpf', ondelete='NO ACTION', onupdate='CASCADE'), index=True)
    codBarras = sa.Column(sa.INTEGER, sa.ForeignKey('tbProduto.codBarras', ondelete='NO ACTION', onupdate='CASCADE'), index=True)
    registro_vendedor = sa.Column(sa.INTEGER, sa.ForeignKey('tbVendedor.registro_vendedor', ondelete='NO ACTION', onupdate='CASCADE'), index=True)
    dia_hora_venda = sa.Column(sa.DATETIME, nullable = False)
    vlrVenda = sa.Column(sa.DECIMAL(10,2), nullable = False)


#Criar a tabelas
try:
    base.metadata.create_all(engine) #Criar a tabela
    #Mensagem de conclusão
    print("Tabelas Criadas!")
except ValueError:
    print("Tabelas NÃO foram criadas. Favor verificar!")