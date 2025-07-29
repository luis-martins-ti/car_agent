FROM python:3.11-slim


RUN apt-get update && apt-get install -y curl git build-essential libpq-dev

ENV POETRY_VERSION=1.8.2
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /car_agent

ENV PYTHONPATH=/car_agent

COPY . .

COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-interaction


CMD ["poetry", "run", "python", "main.py"]
