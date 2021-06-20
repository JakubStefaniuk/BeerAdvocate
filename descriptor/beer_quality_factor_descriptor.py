from provider.data_provider import DataProvider
from result.quality.beer_quality_factor_result import BeerQualityFactorResult


class BeerQualityFactorDescriptor:

    data_provider: DataProvider

    def __init__(self, data_provider: DataProvider):
        self.data_provider = data_provider

    def compute_beer_quality_factors(self) -> list[BeerQualityFactorResult]:
        return []
