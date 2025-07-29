# 🚗 Car Agent – Desafio Técnico Python | C2S
Agente virtual via terminal que conversa com o usuário em linguagem natural e ajuda a encontrar veículos com base em suas preferências.

Utiliza:

**Python + SQLAlchemy + PostgreSQL**

**OpenAI SDK (via Open Router AI)**

**Mistral - mistral-7b Model**

**Model Context Protocol (MCP) proprietário para organizar o contexto**

**Docker + Poetry para instalação e execução**
---

## 🚀 Como iniciar o projeto

### ✅ Pré-requisitos
- Docker
- Docker Compose

---

### 🧱 STEP 1 - Build e start com Docker

**Renomeie o arquivo .env.example para .env, insira sua chave Open Router em OPENROUTER_API_KEY e execute no terminal:**

**Caso necessário gere sua chave gratuitamente em openrouter.ai**

```bash
docker compose build --no-cache
docker compose up -d
```


### 📦 STEP 2 - Criar banco e aplicar Seed:

```bash
#Acesse o container
docker compose exec -it car-agent bash
#registre os scripts executáveis
poetry install
#rode a seed
poetry run python car_agent/db/seed.py
```

### 🖥️ STEP 3 - Iniciar a aplicação

```bash
poetry run car-agent
```

### 🤖 Como usar o agente

Você verá algo como:

```bash
Bem-vindo ao assistente de veículos!
Você:
Digite em linguagem natural:
```

Exemplos:
"Quero um SUV flex até 80 mil"

"Procuro um sedã preto automático entre 2015 e 2020"

"Me mostra um carro econômico com motor 1.0"

O agente entenderá sua intenção, montará o contexto (MCP), enviará para a LLM e retornará veículos compatíveis do banco de dados.
Para sair basta digitar **sair**

🔍 **Filtros interpretados**
O agente pode aplicar filtros como:

- marca
- modelo
- ano mínimo/máximo
- motor
- tipo de combustível
- cor
- quilometragem máxima
- faixa de preço
- número de portas
- transmissão

### 🧪 TESTES:

```bash
poetry run pytest
```


### 📘 Tecnologias Utilizadas
- Python
- Poetry
- PostgreSQL
- Sql Alchemy
- Docker
- OpenAI SDK
- Mistral - mistral-7b Model
- PyTest

**Para remover a aplicação rodar:**
```bash
docker compose down -v --remove-orphans
```