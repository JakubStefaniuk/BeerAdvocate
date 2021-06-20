from descriptor.beer_abv_descriptor import BeerAbvDescriptor
from descriptor.beer_quality_factor_descriptor import BeerQualityFactorDescriptor
from provider.csv_data_provider import CsvDataProvider
from provider.data_provider import DataProvider


def describe_beer_abv(data_provider: DataProvider):
    beer_abv_descriptor = BeerAbvDescriptor(data_provider)
    max_beer_abv = beer_abv_descriptor.compute_highest_beer_abv()
    max_beer_mean_abv = beer_abv_descriptor.compute_highest_abv_mean()
    print(f"- {max_beer_abv.describe()}")
    print(f"- {max_beer_mean_abv.describe()}")


def describe_beer_quality_factors(data_provider: DataProvider):
    beer_quality_descriptor = BeerQualityFactorDescriptor(data_provider)
    most_crucial_factors = beer_quality_descriptor.compute_beer_quality_factors()
    for factor in most_crucial_factors:
        print(f"- {factor.describe()}")


if __name__ == '__main__':
    csv_data_provider = CsvDataProvider('beer_reviews.csv', ',')
    print("Beer abv:")
    describe_beer_abv(csv_data_provider)
    print("Quality factors:")
    describe_beer_quality_factors(csv_data_provider)

