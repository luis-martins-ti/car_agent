import os
from sqlalchemy import Column, Integer, String, Numeric, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


Base = declarative_base()
DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


class Veiculo(Base):
    __tablename__ = "veiculos"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    motor = Column(String)
    combustivel = Column(String)
    cor = Column(String)
    km = Column(Integer)
    preco = Column(Numeric(10, 2))
    portas = Column(Integer)
    transmissao = Column(String)


def criar_tabelas():
    Base.metadata.create_all(bind=engine)
