from result.beer_adv_result import BeerAdvResult


class MaxBeerAdvResult(BeerAdvResult):

    brewery_name: str
    max_beer_adv: float

    def __init__(self, brewery_name: str, max_beer_adv: float):
        self.brewery_name = brewery_name
        self.max_beer_adv = max_beer_adv

    def describe(self) -> str:
        return f"Strongest beer is produced by {self.brewery_name} brewery and its abv is {self.max_beer_adv}%"
