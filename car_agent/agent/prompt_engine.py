from openai import OpenAI
import os
import re
import json

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


def extract_json(text: str) -> dict:
    def normalize_value(value):
        if value in [None, 0, 0.0]:
            return ""
        return value

    try:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            data = json.loads(match.group())
            # Normaliza os valores
            return {k: normalize_value(v) for k, v in data.items()}
    except Exception as e:
        print("Erro ao extrair JSON:", e)
    return {}


def ask_llm(prompt: str) -> dict:
    try:
        response = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct:free",
            messages=[
                {
                    "role": "system",
                    "content": "Você é um assistente especialista em carros.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.4,
        )
        content = response.choices[0].message.content
        return extract_json(content)
    except Exception as e:
        print("Erro ao interpretar a resposta da LLM:", e)
        return {}
