from models import Conta, engine, Bancos
from sqlmodel import Session, select


def criar_conta(conta: Conta):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.banco=='INTER')
        results = session.exec(statement).all
        print (results)

        #session.add(conta)
        #session.commit()

#Variavel que vai conter valores dinâmicos 
conta = Conta(valor=20, banco=Bancos.NUBANK)
criar_conta(conta)

!Finalizei o vídeo em 56 MINUTOS