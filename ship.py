class Ship:
    def __init__(self, region, fuel):
        self.region = region
        self.fuel = fuel

    def travel_to_region(self, region):
        self.region = region

    def get_region(self):
        return self.region
