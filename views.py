from models import Conta, engine, Bancos, Status #Importar Conta: que vem de models, engine: conecção com datebase.db e Bancos: emuneração opções
from sqlmodel import Session, select #Pacote python sql e duas tags (Session-Inicia a conecção com o banco de dados e select-que procura a tabela)


def criar_conta(conta: Conta):
    with Session(engine) as session: #Ligação com datebase.db atraves da tag Session(qual banco de dados?) as 'nome que quero chamar a sessão'
        statement = select(Conta).where(Conta.banco==conta.banco) #Seleciona qual tabela acessar e filtro com WHERE e com comparação de colunas
        results = session.exec(statement).all() #Execulto com a tag EXEC(qual tabela?) e afirmo que é todas as linhas com ALL()
        
        if results: #Validação de existecia de conta
            print('Já existe uma conta nesse banco!')
            return

    session.add(conta) #Adiciona a conta em state(Porém não envia para banco de dados)
    session.commit() #Cria e envia para o banco de danos
    print(f'conta {Bancos} criada com sucesso!')
    return conta #Retorna o parametro da função


def listar_contas():
    with Session(engine) as session:
        statement = select(Conta)
        results = session.exec(statement).all()
        return results

def desativar_conta(id):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id==id)
        conta = session.exec(statement).first()
        
        if conta.valor > 0:
            raise ValueError('Essa conta tem saldo')
        conta.status = Status.INATIVO
        session.commit()


#Variavel que vai conter valores dinâmicos 
conta = Conta(valor=10, banco=Bancos.NUBANK)
criar_conta(conta)
desativar_conta(1)
