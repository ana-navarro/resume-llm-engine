from dataclasses import dataclass

from domain.models.prompt_sections import PromptSections


@dataclass(frozen=True)
class PersonaPrompt:
    sections: PromptSections
    final_prompt: str
