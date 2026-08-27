from abc import ABC, abstractmethod


class GetPersonaContextPort(ABC):
    @abstractmethod
    def execute(self) -> str:
        raise NotImplementedError
