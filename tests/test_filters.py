import pytest
from car_agent.search.filters import buscar_veiculos
from car_agent.db.models import Veiculo, SessionLocal


@pytest.fixture
def db_session_with_veiculos():
    session = SessionLocal()

    session.query(Veiculo).delete()

    veiculos = [
        Veiculo(
            marca="Fiat",
            modelo="Uno",
            ano=2015,
            motor="1.0",
            combustivel="Flex",
            cor="Preto",
            km=80000,
            preco=28000,
            portas=4,
            transmissao="Manual",
        ),
        Veiculo(
            marca="Fiat",
            modelo="Argo",
            ano=2019,
            motor="1.3",
            combustivel="Flex",
            cor="Vermelho",
            km=40000,
            preco=45000,
            portas=4,
            transmissao="Automática",
        ),
        Veiculo(
            marca="Ford",
            modelo="Ka",
            ano=2016,
            motor="1.0",
            combustivel="Flex",
            cor="Preto",
            km=75000,
            preco=30000,
            portas=4,
            transmissao="Manual",
        ),
    ]

    session.add_all(veiculos)
    session.commit()
    yield
    session.close()


def test_busca_por_marca(db_session_with_veiculos):
    filtros = {"marca": "Fiat"}
    resultado = buscar_veiculos(filtros)
    assert isinstance(resultado, list)
    assert all("Fiat" in v.marca for v in resultado)
