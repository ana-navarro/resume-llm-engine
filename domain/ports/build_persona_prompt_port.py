from abc import ABC, abstractmethod

from domain.models.persona_prompt import PersonaPrompt


class BuildPersonaPromptPort(ABC):
    @abstractmethod
    def execute(self) -> PersonaPrompt:
        raise NotImplementedError
