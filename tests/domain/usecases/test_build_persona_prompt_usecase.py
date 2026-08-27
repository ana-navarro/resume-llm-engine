from unittest.mock import Mock

from domain.usecases.build_persona_prompt_usecase import BuildPersonaPromptUseCase


def _build_usecase():
    ports = {
        "get_persona_rules": Mock(),
        "get_persona_context": Mock(),
        "get_persona_tone": Mock(),
    }
    ports["get_persona_rules"].execute.return_value = "rules text"
    ports["get_persona_context"].execute.return_value = "context text"
    ports["get_persona_tone"].execute.return_value = "tone text"
    return BuildPersonaPromptUseCase(**ports), ports


def test_execute_combines_all_three_sections():
    usecase, ports = _build_usecase()

    result = usecase.execute()

    ports["get_persona_rules"].execute.assert_called_once_with()
    ports["get_persona_context"].execute.assert_called_once_with()
    ports["get_persona_tone"].execute.assert_called_once_with()

    assert result.sections.rules == "rules text"
    assert result.sections.context == "context text"
    assert result.sections.tone_of_voice == "tone text"


def test_execute_final_prompt_contains_all_sections_in_order():
    usecase, _ = _build_usecase()

    result = usecase.execute()

    rules_index = result.final_prompt.index("rules text")
    context_index = result.final_prompt.index("context text")
    tone_index = result.final_prompt.index("tone text")
    assert rules_index < context_index < tone_index
    assert "## Rules" in result.final_prompt
    assert "## Context" in result.final_prompt
    assert "## Tone of Voice" in result.final_prompt
