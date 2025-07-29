from car_agent.agent.mcp import MCPContext
from car_agent.agent.prompt_engine import extract_json


def test_mcp_prompt_format():
    context = MCPContext()
    context.add_interaction("Quero um carro Fiat preto automático")
    prompt = context.build_prompt()
    assert "Formato esperado" in prompt
    assert "Histórico" in prompt
    assert "marca" in prompt


def test_extract_json_valido():
    entrada = """
    {
        "marca": "Fiat",
        "cor": "preto",
        "transmissao": "Automática"
    }
    """
    saida = extract_json(entrada)
    assert saida == {"marca": "Fiat", "cor": "preto", "transmissao": "Automática"}


def test_extract_json_invalido():
    entrada = "Texto qualquer sem JSON"
    saida = extract_json(entrada)
    assert saida == {}
