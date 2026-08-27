from domain.models.persona_prompt import PersonaPrompt
from domain.models.prompt_sections import PromptSections
from domain.ports.build_persona_prompt_port import BuildPersonaPromptPort
from infra.ports.get_persona_context_port import GetPersonaContextPort
from infra.ports.get_persona_rules_port import GetPersonaRulesPort
from infra.ports.get_persona_tone_port import GetPersonaTonePort


class BuildPersonaPromptUseCase(BuildPersonaPromptPort):
    def __init__(
        self,
        get_persona_rules: GetPersonaRulesPort,
        get_persona_context: GetPersonaContextPort,
        get_persona_tone: GetPersonaTonePort,
    ) -> None:
        self._get_persona_rules = get_persona_rules
        self._get_persona_context = get_persona_context
        self._get_persona_tone = get_persona_tone

    def execute(self) -> PersonaPrompt:
        sections = PromptSections(
            rules=self._get_persona_rules.execute(),
            context=self._get_persona_context.execute(),
            tone_of_voice=self._get_persona_tone.execute(),
        )
        final_prompt = (
            f"## Rules\n{sections.rules}\n\n"
            f"## Context\n{sections.context}\n\n"
            f"## Tone of Voice\n{sections.tone_of_voice}"
        )
        return PersonaPrompt(sections=sections, final_prompt=final_prompt)
