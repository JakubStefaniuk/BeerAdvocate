import pandas as pd
from pandas import DataFrame

from provider.data_provider import DataProvider


class CsvDataProvider(DataProvider):

    def __init__(self, dataset_name, delimiter=','):
        self.data = pd.read_csv(dataset_name, delimiter=delimiter)

    def get_data(self) -> DataFrame:
        return self.data
