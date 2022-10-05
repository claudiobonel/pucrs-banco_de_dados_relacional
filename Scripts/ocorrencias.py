#Primeira coisa a se fazer é importar o SQLAlchemy para utilizar os métodos no Python
import sqlalchemy as sa 

#Agora, vamos criar uma engrenagem com o Banco de dados.
#Para nossa disciplina, utilizaremos o SQLite
engine = sa.create_engine("sqlite:///BD//Ocorrencias.db")

#Uma vez com a engrenagem de banco conectada, precisamos de importar
#um dos principais métodos do SQLAlchemy, que é a declarative_base()

#Esse método é, literalmente, a BASE para a realização do Mapeamento
#dos objetos no SQLite. É ele que vai te possibilitar a criação de uma classe
#para, consequente, criação das tabelas e colunas.
import sqlalchemy.orm as orm
base = orm.declarative_base() #variável de ORM

#criando tbDP, via ORM
class dp(base):
    __tablename__ = 'tbDP'

    codDP = sa.Column(sa.INTEGER, primary_key = True, index=True)
    nmDP = sa.Column(sa.VARCHAR(100), nullable = False)
    enderecoDP = sa.Column(sa.VARCHAR(255), nullable = False) 

#criando tbResponsavelDP, via ORM
class responsaveldp(base):
    __tablename__ = 'tbResponsavelDP'

    codDP = sa.Column(sa.INTEGER, primary_key = True,index=True)
    delegado = sa.Column(sa.VARCHAR(100), nullable = False)

#criando tbMunicipio, via ORM
class municipio(base):
    __tablename__ = 'tbMunicipio'

    codIBGE = sa.Column(sa.INTEGER, primary_key = True,index=True)
    municipio = sa.Column(sa.VARCHAR(100), nullable = False)
    regiao = sa.Column(sa.VARCHAR(25), nullable = False)

#criando tbOcorrencias, via ORM
class ocorrencia(base):
    __tablename__ = 'tbOcorrencias'

    idRegistro = sa.Column(sa.INTEGER, primary_key = True, index=True)
    codDP = sa.Column(sa.INTEGER, sa.ForeignKey('tbDP.codDP', ondelete='NO ACTION', onupdate='CASCADE'), index=True)
    codIBGE = sa.Column(sa.INTEGER, sa.ForeignKey('tbMunicipio.codIBGE', ondelete='NO ACTION', onupdate='CASCADE'), index=True)
    ano = sa.Column(sa.CHAR(4), nullable=False)
    mes = sa.Column(sa.CHAR(2), nullable=False)
    ocorrencia = sa.Column(sa.VARCHAR(100), nullable = False)
    qtde = sa.Column(sa.INTEGER, nullable=False)

#Criar a tabelas
try:
    base.metadata.create_all(engine) #Criar a tabela
    #Mensagem de conclusão
    print("Tabelas Criadas!")
except ValueError:
    print("Tabelas NÃO foram criadas. Favor verificar!")


