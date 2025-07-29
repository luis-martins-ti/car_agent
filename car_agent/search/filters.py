from car_agent.db.models import SessionLocal, Veiculo


def buscar_veiculos(filtros: dict):
    session = SessionLocal()
    query = session.query(Veiculo)

    if filtros.get("marca"):
        query = query.filter(Veiculo.marca.ilike(f"%{filtros['marca']}%"))
    if filtros.get("modelo"):
        query = query.filter(Veiculo.modelo.ilike(f"%{filtros['modelo']}%"))
    if filtros.get("ano_minimo") not in [None, ""]:
        query = query.filter(Veiculo.ano >= filtros["ano_minimo"])
    if filtros.get("ano_maximo") not in [None, ""]:
        query = query.filter(Veiculo.ano <= filtros["ano_maximo"])
    if filtros.get("motor"):
        query = query.filter(Veiculo.motor.ilike(f"%{filtros['motor']}%"))
    if filtros.get("combustivel"):
        query = query.filter(Veiculo.combustivel.ilike(f"%{filtros['combustivel']}%"))
    if filtros.get("cor"):
        query = query.filter(Veiculo.cor.ilike(f"%{filtros['cor']}%"))
    if filtros.get("km_max") not in [None, ""]:
        query = query.filter(Veiculo.km <= filtros["km_max"])
    if filtros.get("preco_min") not in [None, ""]:
        query = query.filter(Veiculo.preco >= filtros["preco_min"])
    if filtros.get("preco_max") not in [None, ""]:
        query = query.filter(Veiculo.preco <= filtros["preco_max"])
    if filtros.get("portas") not in [None, ""]:
        query = query.filter(Veiculo.portas == filtros["portas"])
    if filtros.get("transmissao"):
        query = query.filter(Veiculo.transmissao.ilike(f"%{filtros['transmissao']}%"))

    resultados = query.limit(10).all()
    session.close()
    return resultados
