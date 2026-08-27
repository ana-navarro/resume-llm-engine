from dataclasses import dataclass


@dataclass(frozen=True)
class PromptSections:
    rules: str
    context: str
    tone_of_voice: str
