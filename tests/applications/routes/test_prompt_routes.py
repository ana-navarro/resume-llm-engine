from unittest.mock import Mock

from fastapi import FastAPI
from fastapi.testclient import TestClient

from applications.routes import prompt_routes


def _build_app():
    app = FastAPI()
    app.include_router(prompt_routes.router)
    return app


def test_get_prompt_returns_the_built_persona_prompt(monkeypatch):
    fake_controller = Mock()
    fake_controller.handle.return_value = {
        "rules": "r",
        "context": "c",
        "tone_of_voice": "t",
        "final_prompt": "## Rules\nr\n\n## Context\nc\n\n## Tone of Voice\nt",
    }
    monkeypatch.setattr(prompt_routes, "_controller", fake_controller)

    client = TestClient(_build_app())
    response = client.get("/prompt")

    assert response.status_code == 200
    assert response.json() == fake_controller.handle.return_value
