from infra.adapters.get_persona_context_adapter import (
    CONTEXT_TEXT,
    GetPersonaContextAdapter,
)


def test_execute_returns_the_hardcoded_context_text():
    assert GetPersonaContextAdapter().execute() == CONTEXT_TEXT


def test_context_text_mentions_career_objective_and_interpersonal_skills():
    assert "career objective" in CONTEXT_TEXT.lower()
    assert "interpersonal skills" in CONTEXT_TEXT.lower()
