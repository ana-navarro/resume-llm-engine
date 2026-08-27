# resume-llm-engine

## Papel no ecossistema (PT)

Motor de Inferência do Currículo Interativo. Configura o modelo de LLM, aplica a persona do assistente
(baseada no currículo de Ana Elisa) e executa a chamada real para a API de IA (ver Constitution
Principle I, `.specify/memory/constitution.md`).

Fluxo de chamadas estrito (Constitution Principle II): `Frontend → bff → orchestrator → (guard-rails,
embeddings, llm-engine)`. Este serviço só deve ser chamado pelo `resume-orchestrator`, após os dados
terem passado (quando aplicável) por `resume-guard-rails` e `resume-embeddings`.

## Status atual

Primeira feature real: `GET /prompt` monta o "system prompt" da persona do assistente a partir de 3
pilares (Constitution Principle I — "aplica a persona"), cada um buscado via seu próprio port/adapter
de Output:

- **Rules**: regras estritas de comportamento (nunca inventar experiências/habilidades fora do
  currículo, admitir quando não souber, não revelar o prompt de sistema, responder no idioma do
  usuário).
- **Context**: informações fixas que não vêm dos PDFs (objetivo de carreira, habilidades
  interpessoais) — **conteúdo placeholder** (`infra/adapters/get_persona_context_adapter.py`),
  precisa ser substituído pelo conteúdo real de Ana Elisa antes de uso em produção.
- **Tone of Voice**: profissional, empático, resolutivo.

**Fora de escopo desta feature** (tasks futuras): mesclar conteúdo do currículo/embeddings, histórico
de chat, e a chamada real à API do provedor de LLM — `resume-llm-engine` ainda não faz nenhuma das
duas.

## Stack

- Python + FastAPI
- `pytest` + `pytest-cov` (testes, cobertura mínima de 80% — Constitution Principle III)
- `ruff` (lint)
- Integração com provedor de LLM (a definir — task futura)

## Como rodar localmente

```sh
python -m venv .venv
.venv/Scripts/activate       # Windows
# source .venv/bin/activate  # Linux/Mac
pip install -r requirements-dev.txt
uvicorn main:app --reload
```

## Rodando a pipeline local (lint + testes + cobertura)

```sh
make validate-pipeline
```

Em ambientes sem `make` (ex.: Git Bash no Windows), rode os passos equivalentes diretamente:

```sh
python -m ruff check .
python scripts/gen_coveragerc.py
python -m pytest --cov --cov-config=.coveragerc --cov-report=term-missing
```

## Role in the ecosystem (EN)

The inference engine. Configures the LLM, applies the assistant's persona, and makes the actual call
to the AI API. First real feature implemented: `GET /prompt`, which assembles the persona's system
prompt from 3 pillars — Rules, Context, and Tone of Voice — each behind its own Output port/adapter.
The "Context" pillar's content is a placeholder pending the candidate's real career objective and
interpersonal skills. Merging in resume/embeddings content, chat history, and the actual LLM API call
are out of scope for now.
