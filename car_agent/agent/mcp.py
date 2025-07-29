class MCPContext:
    def __init__(self):
        self.task_description = "Você é um especialista em carros e deve ajudar o usuário a encontrar um carro com base em suas preferências."
        self.interactions = []
        self.rules = [
            "Nunca repita perguntas já feitas.",
            "Retorne SOMENTE um JSON puro com os filtros inferidos. Não escreva explicações nem texto fora do JSON.",
            "O filtro transmissao deve ser apenas uma das opções Manual, Automática ou CVT",
            "O filtro combustivel deve ser apenas uma das opções Gasolina Etanol, Flex, Diesel ou GNV",
            "Não defina ano_minimo e ano_maximo se não for solicitado filtro por ano",
            "Só faça perguntas se realmente necessário.",
        ]
        self.expected_format = {
            "marca": "string",
            "modelo": "string",
            "ano_minimo": "int",
            "ano_maximo": "int",
            "motor": "string",
            "combustivel": "string",
            "cor": "string",
            "km_max": "int",
            "preco_min": "float",
            "preco_max": "float",
            "portas": "int",
            "transmissao": "string",
        }

    def add_interaction(self, user_input: str, agent_response: str = None):
        self.interactions.append({"user": user_input})
        if agent_response:
            self.interactions.append({"agent": agent_response})

    def build_prompt(self) -> str:
        history = "\n".join(
            [
                f"{'Usuário' if 'user' in i else 'Agente'}: {i.get('user') or i.get('agent')}"
                for i in self.interactions
            ]
        )
        rules = "\n".join(f"- {rule}" for rule in self.rules)
        fmt = "\n".join(f"- {k}: {v}" for k, v in self.expected_format.items())
        return f"""
Tarefa: {self.task_description}

Regras:
{rules}

Histórico:
{history}

Formato esperado:
{fmt}

Retorne um JSON com os filtros inferidos até agora.
"""
