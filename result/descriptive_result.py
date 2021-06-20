from abc import ABC, abstractmethod


class DescriptiveResult(ABC):

    @abstractmethod
    def describe(self) -> str:
        pass
