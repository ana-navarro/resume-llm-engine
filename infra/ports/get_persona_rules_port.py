from abc import ABC, abstractmethod


class GetPersonaRulesPort(ABC):
    @abstractmethod
    def execute(self) -> str:
        raise NotImplementedError
