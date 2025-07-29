from car_agent.search.filters import buscar_veiculos


def test_busca_por_marca():
    filtros = {"marca": "Fiat"}
    resultado = buscar_veiculos(filtros)
    assert isinstance(resultado, list)
