from domain.ports.build_persona_prompt_port import BuildPersonaPromptPort


class GetPersonaPromptController:
    def __init__(self, build_persona_prompt: BuildPersonaPromptPort) -> None:
        self._build_persona_prompt = build_persona_prompt

    def handle(self) -> dict:
        persona_prompt = self._build_persona_prompt.execute()
        return {
            "rules": persona_prompt.sections.rules,
            "context": persona_prompt.sections.context,
            "tone_of_voice": persona_prompt.sections.tone_of_voice,
            "final_prompt": persona_prompt.final_prompt,
        }
