from result.descriptive_result import DescriptiveResult


class BeerQualityFactorResult(DescriptiveResult):

    factor_name: str
    impact_percent: float

    def __init__(self, factor_name: str, impact_percent: float):
        self.factor_name = factor_name
        self.impact_percent = impact_percent

    def describe(self) -> str:
        return f"Factor: {self.factor_name} impacts beer quality, having: {self.impact_percent}% influence"
