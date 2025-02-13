from sqlmodel import SQLModel, Field, create_engine
from enum import Enum


#Class de Opçoes de bancos - Enumerações
class Bancos(Enum):
    NUBANK = 'Nubank'
    SANTANDER = 'Santander'
    INTER = 'Inter'

#Class de Opçoes Status - Enumerações
class Status(Enum):
    ATIVO = "Ativo"
    INATIVO = "Inativo"


#Class para criar a tabelas no banco de dados
class conta(SQLModel, table=True):
    id: int = Field(primary_key=True)
    valor: float
    banco: Bancos = Field(default=Bancos.NUBANK)
    status: Status = Field(default=Status.ATIVO)

#Varieavel que vai conter o nome do banco de dados e o caminho para a conexão
sqlite_file_name = 'datebase.db'
sqlite_url = f"sqlite:///{sqlite_file_name}"

#conectar a tabela ao banco (Importar a biblioteca de ligação-Create engine)
engine = create_engine(sqlite_url, echo=True)

#Criar o banco de dados - do tipo SQLModel, um arquivo "metadata" e criar todas as tabelas que está na var=engine
if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)


