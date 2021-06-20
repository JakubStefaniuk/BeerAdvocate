from result.beer_adv_result import BeerAdvResult


class BeerAdvMeanMaxResult(BeerAdvResult):

    brewery_name: str
    max_adv_mean: float

    def __init__(self, brewery_name: str, max_mean: float):
        self.brewery_name = brewery_name
        self.max_mean = max_mean

    def describe(self) -> str:
        return f"Brewery {self.brewery_name} produces highest adv beers on average; {self.max_mean:.2f}%"


