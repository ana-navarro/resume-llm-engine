from abc import ABC, abstractmethod


class GetPersonaTonePort(ABC):
    @abstractmethod
    def execute(self) -> str:
        raise NotImplementedError
