# resume-llm-engine

## Papel no ecossistema (PT)

Motor de Inferência do Currículo Interativo. Configura o modelo de LLM, aplica a persona do assistente
(baseada no currículo de Ana Elisa) e executa a chamada real para a API de IA (ver Constitution
Principle I, `.specify/memory/constitution.md`).

Fluxo de chamadas estrito (Constitution Principle II): `Frontend → bff → orchestrator → (guard-rails,
embeddings, llm-engine)`. Este serviço só deve ser chamado pelo `resume-orchestrator`, após os dados
terem passado (quando aplicável) por `resume-guard-rails` e `resume-embeddings`.

## Status atual

Stub inicial (FastAPI "Hello World", `main.py`) — nenhuma lógica de inferência/persona foi implementada
ainda. A estrutura hexagonal completa (`applications/`, `domain/`, `infra/`, `config/`) descrita na
Constitution Principle II ainda não foi criada neste serviço.

## Stack

- Python + FastAPI
- Integração com provedor de LLM (a definir)

## Como rodar localmente

```sh
python -m venv .venv
.venv/Scripts/activate       # Windows
# source .venv/bin/activate  # Linux/Mac
pip install fastapi "uvicorn[standard]"
uvicorn main:app --reload
```

## Role in the ecosystem (EN)

The inference engine. Configures the LLM, applies the assistant's persona (based on Ana Elisa's resume),
and makes the actual call to the AI API. Currently a stub — only the FastAPI "Hello World" endpoint
exists.
