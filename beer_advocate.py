from descriptor.beer_adv_descriptor import BeerAdvDescriptor
from provider.csv_data_provider import CsvDataProvider
from provider.data_provider import DataProvider


def describe_beer_adv(data_provider: DataProvider):
    beer_adv_descriptor = BeerAdvDescriptor(data_provider)
    max_beer_adv = beer_adv_descriptor.compute_highest_beer_adv()
    max_beer_mean_adv = beer_adv_descriptor.compute_highest_adv_mean()
    print(max_beer_adv.describe())
    print(max_beer_mean_adv.describe())


if __name__ == '__main__':
    csv_data_provider = CsvDataProvider('beer_reviews.csv', ',')
    describe_beer_adv(csv_data_provider)
