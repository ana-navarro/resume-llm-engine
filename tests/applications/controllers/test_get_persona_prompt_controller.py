from unittest.mock import Mock

from applications.controllers.get_persona_prompt_controller import (
    GetPersonaPromptController,
)
from domain.models.persona_prompt import PersonaPrompt
from domain.models.prompt_sections import PromptSections


def test_handle_formats_the_persona_prompt():
    build_persona_prompt = Mock()
    build_persona_prompt.execute.return_value = PersonaPrompt(
        sections=PromptSections(rules="r", context="c", tone_of_voice="t"),
        final_prompt="## Rules\nr\n\n## Context\nc\n\n## Tone of Voice\nt",
    )
    controller = GetPersonaPromptController(build_persona_prompt)

    result = controller.handle()

    assert result == {
        "rules": "r",
        "context": "c",
        "tone_of_voice": "t",
        "final_prompt": "## Rules\nr\n\n## Context\nc\n\n## Tone of Voice\nt",
    }
