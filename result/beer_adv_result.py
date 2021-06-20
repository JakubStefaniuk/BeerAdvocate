from abc import ABC, abstractmethod


class BeerAdvResult(ABC):

    @abstractmethod
    def describe(self) -> str:
        pass
