class Ship:
    def __init__(self, region, fuel):
        self.region = region
        self.fuel = fuel

    def travel_to_region(self, region):
        self.region = region
        #TODO: remove fuel in further interations.