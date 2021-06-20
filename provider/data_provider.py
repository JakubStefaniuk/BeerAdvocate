from abc import ABC, abstractmethod

from pandas import DataFrame


class DataProvider(ABC):

    @abstractmethod
    def get_data(self) -> DataFrame:
        pass
