from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import DECIMAL

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'
    # atributos
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(11), unique=True, nullable=False)
    endereco = Column(String, unique=True)

    conta = relationship('Conta', back_populates='cliente')

    def __repr__(self):
        return f'Pessoa(id={self.id}, nome={self.nome}, cpf={self.cpf})'

class Conta(Base):
    __tablename__ = 'conta'
    # atributos
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    numero = Column(Integer, ForeignKey('cliente.id'))
    saldo = Column(DECIMAL)

    cliente = relationship('Cliente', back_populates='conta')

    def __repr__(self):
        return f'Conta(id={self.id}, tipo={self.tipo}, agencia={self.agencia}, numero={self.agencia})'


print(Cliente.__tablename__)
print(Conta.__tablename__)

# conexão com banco de dados
engine = create_engine('sqlite://')

# criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)


inspetor_engine = inspect(engine)
#print(inspetor_engine.hastable('conta'))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)


with Session(engine) as session:
    joao = Cliente(
        nome='joao',
        cpf='18456493676',
        endereco='Rua Embaixada, 123'
    )

    matheus = Cliente(
        nome='matheus',
        cpf='15406784523',
        endereco='Rua Canada,254'
    )

    rodrigo = Cliente(
        nome='rodrigo',
        cpf='18453795623',
        endereco='Rua Esperança, 41'
    )

    lucas = Cliente(
        nome='lucas',
        cpf='94615475692',
        endereco='Rua das Aves, 562'
    )

    vinicius = Cliente(
        nome='vinicius',
        cpf='17583563412',
        endereco='Rua Castelo Branco, 426'
    )

    conta_joao = Conta(
        tipo='Conta corrente',
        agencia='0001',
        numero=1,
        saldo=546.00
    )

    conta_matheus = Conta(
        tipo='Conta corrente',
        agencia='0001',
        numero=2,
        saldo=468.31
    )

    conta_rodrigo = Conta(
        tipo='Conta corrente',
        agencia='0001',
        numero=3,
        saldo=247.12
    )

    conta_lucas = Conta(
        tipo='Conta corrente',
        agencia='0001',
        numero=4,
        saldo=10.00
    )

    conta_vinicius = Conta(
        tipo='Conta corrente',
        agencia='0001',
        numero=5,
        saldo=2456.30
    )

    session.add_all([joao, matheus, rodrigo, lucas, vinicius, conta_joao, conta_matheus, conta_rodrigo, conta_lucas, conta_vinicius])

    session.commit()

stmt = select(Cliente).where(Cliente.nome.in_(['joao', 'lucas']))
print('\nRecuperando os cliente')
for cliente in session.scalars(stmt):
    print(cliente)

stmt_conta = select(Conta).where(Conta.numero.in_([1, 4]))
print('\nRecuperando as contas')
for conta in session.scalars(stmt_conta):
    print(conta)

stmt_order = select(Cliente).order_by(Cliente.nome.asc())
print('\nRecuperando informações de forma ordenada')
for result in session.scalars(stmt_order):
    print(result)

stmt_join = select(Cliente, Conta.tipo).join_from(Cliente, Conta)
'''print('\nUtilizando join')
for result in session.scalars(stmt_join):
    print(result)'''

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print('\nUtilizando join')
for result in results:
    print(result)

stmt_count = select(func.count('*')).select_from(Cliente)
print('\nTotal de instâncias em Cliente')
for result in session.scalars(stmt_count):
    print(result)

session.close()

