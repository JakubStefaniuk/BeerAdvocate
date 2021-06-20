
from constants.beer_reviews_columns_constants import BeerReviewsColumnsConstants as Constants
from provider.data_provider import DataProvider
from result.quality.beer_quality_factor_result import BeerQualityFactorResult
from sklearn.preprocessing import OrdinalEncoder
import pandas as pd
pd.options.mode.chained_assignment = None

assumed_possible_quality_factors = [
    Constants.beer_abv(),
    Constants.brewery_id(),
    Constants.beer_style(),
    Constants.appearance_review(),
    Constants.palate_review(),
    Constants.taste_review(),
    Constants.aroma_review()
]


class BeerQualityFactorDescriptor:
    data_provider: DataProvider

    def __init__(self, data_provider: DataProvider):
        self.data_provider = data_provider

    def compute_beer_quality_factors(self) -> list[BeerQualityFactorResult]:
        independent_target_columns = assumed_possible_quality_factors + [Constants.overall_review()]
        dataset = self.data_provider.get_data()[independent_target_columns]
        dataset[Constants.beer_style()] = OrdinalEncoder().fit_transform(dataset[[Constants.beer_style()]])
        correlation_results = dataset.corr(method='pearson')[Constants.overall_review()][:-1].reset_index()
        sorted_results = correlation_results.sort_values(by=Constants.overall_review(), ascending=False)[:3]
        factor_results = sorted_results.apply(self.to_factor_result, axis=1)
        return factor_results

    def to_factor_result(self, row) -> BeerQualityFactorResult:
        return BeerQualityFactorResult(row['index'], row[Constants.overall_review()])
