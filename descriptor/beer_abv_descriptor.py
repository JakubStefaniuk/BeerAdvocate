from provider.data_provider import DataProvider
from constants.beer_reviews_columns_constants import BeerReviewsColumnsConstants as Constants
from result.adv.beer_abv_mean_max_result import BeerAbvMeanMaxResult
from result.adv.max_beer_abv_result import MaxBeerAbvResult


class BeerAbvDescriptor:

    data_provider: DataProvider

    def __init__(self, data_provider: DataProvider):
        self.data_provider = data_provider

    def compute_highest_beer_abv(self) -> MaxBeerAbvResult:
        dataset = self.data_provider.get_data()
        max_beer_abv_row = dataset.iloc[dataset[Constants.beer_abv()].argmax()]
        return MaxBeerAbvResult(max_beer_abv_row[Constants.brewery_name()], max_beer_abv_row[Constants.beer_abv()])

    def compute_highest_abv_mean(self) -> BeerAbvMeanMaxResult:
        brewery_name_abv_dataset = self.data_provider.get_data()[[Constants.brewery_name(), Constants.beer_abv()]]
        breweries_means = brewery_name_abv_dataset.groupby(Constants.brewery_name()).mean().reset_index()
        max_mean_aggregated_row = breweries_means.iloc[breweries_means[Constants.beer_abv()].argmax()]
        return BeerAbvMeanMaxResult(
            max_mean_aggregated_row[Constants.brewery_name()],
            max_mean_aggregated_row[Constants.beer_abv()]
            )
