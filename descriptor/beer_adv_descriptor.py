from provider.data_provider import DataProvider
from result.beer_adv_mean_max_result import BeerAdvMeanMaxResult
from result.max_beer_adv_result import MaxBeerAdvResult
from constants.beer_reviews_columns_constants import BeerReviewsColumnsConstants as Constants


class BeerAdvDescriptor:

    data_provider: DataProvider

    def __init__(self, data_provider: DataProvider):
        self.data_provider = data_provider

    def compute_highest_beer_adv(self) -> MaxBeerAdvResult:
        dataset = self.data_provider.get_data()
        max_beer_adv_row = dataset.iloc[dataset[Constants.beer_abv()].argmax()]
        return MaxBeerAdvResult(max_beer_adv_row[Constants.brewery_name()], max_beer_adv_row[Constants.beer_abv()])

    def compute_highest_adv_mean(self) -> BeerAdvMeanMaxResult:
        brewery_name_adv_dataset = self.data_provider.get_data()[[Constants.brewery_name(), Constants.beer_abv()]]
        breweries_means = brewery_name_adv_dataset.groupby(Constants.brewery_name()).mean().reset_index()
        max_mean_aggregated_row = breweries_means.iloc[breweries_means[Constants.beer_abv()].argmax()]
        return BeerAdvMeanMaxResult(
            max_mean_aggregated_row[Constants.brewery_name()],
            max_mean_aggregated_row[Constants.beer_abv()]
            )
