from faker import Faker
import random
from car_agent.db.models import Veiculo, criar_tabelas, SessionLocal


def gerar_veiculos(quantidade: int = 100):
    fake = Faker("pt_BR")
    criar_tabelas()
    session = SessionLocal()

    marcas_modelos = {
        "Toyota": ["Corolla", "Hilux", "Yaris", "Etios", "SW4"],
        "Fiat": ["Argo", "Toro", "Pulse", "Mobi", "Strada"],
        "Volkswagen": ["Gol", "T-Cross", "Nivus", "Polo", "Virtus"],
        "Chevrolet": ["Onix", "Tracker", "S10", "Spin", "Cruze"],
        "Hyundai": ["HB20", "Creta", "Tucson", "Santa Fe"],
        "Renault": ["Kwid", "Duster", "Captur", "Sandero"],
        "Honda": ["Civic", "City", "HR-V", "Fit"],
        "Nissan": ["Kicks", "Versa", "March", "Frontier"],
        "Jeep": ["Renegade", "Compass", "Commander"],
        "Peugeot": ["208", "2008", "3008"],
    }

    cores = [
        "Preto",
        "Branco",
        "Prata",
        "Cinza",
        "Vermelho",
        "Azul",
        "Verde",
        "Amarelo",
        "Marrom",
        "Laranja",
    ]

    for _ in range(quantidade):
        marca = random.choice(list(marcas_modelos.keys()))
        modelo = random.choice(marcas_modelos[marca])
        veiculo = Veiculo(
            marca=marca,
            modelo=modelo,
            ano=random.randint(2005, 2025),
            motor=random.choice(["1.0", "1.3", "1.6", "2.0", "2.4"]),
            combustivel=random.choice(["Gasolina", "Etanol", "Flex", "Diesel", "GNV"]),
            cor=random.choice(cores),
            km=random.randint(0, 180000),
            preco=round(random.uniform(25000, 250000), 2),
            portas=random.choice([2, 4, 5]),
            transmissao=random.choice(["Manual", "Automática", "CVT"]),
        )
        session.add(veiculo)

    session.commit()
    session.close()
    print(f"{quantidade} veículos inseridos com sucesso.")


if __name__ == "__main__":
    gerar_veiculos()
