# tests/test_main_flow.py

import pytest
from unittest.mock import patch
from car_agent.db.models import Veiculo, SessionLocal
from car_agent.agent.mcp import MCPContext
from car_agent.search.filters import buscar_veiculos


@pytest.fixture
def db_session_for_flow():
    session = SessionLocal()
    session.query(Veiculo).delete()
    session.add(
        Veiculo(
            marca="Fiat",
            modelo="Argo",
            ano=2019,
            motor="1.3",
            combustivel="Flex",
            cor="Preto",
            km=30000,
            preco=48000,
            portas=4,
            transmissao="Automática",
        )
    )
    session.commit()
    yield
    session.close()


@patch("car_agent.agent.prompt_engine.ask_llm")
def test_fluxo_completo_com_mock_llm(mock_ask_llm, db_session_for_flow):
    mock_ask_llm.return_value = {
        "marca": "Fiat",
        "cor": "preto",
        "transmissao": "Automática",
    }

    context = MCPContext()
    context.add_interaction("Quero um Fiat preto automático")
    prompt = context.build_prompt()
    filtros = mock_ask_llm(prompt)

    resultado = buscar_veiculos(filtros)

    assert isinstance(resultado, list)
    assert len(resultado) == 1
    assert resultado[0].modelo == "Argo"
