class Player:
    def __init__(self, name, skills, ship):
        self.name = name
        self.skills = skills
        self.ship = ship

    @property
    def region(self):
        return self.ship.region

    def travel_to_region(self, region):
        self.ship.travel_to_region(region)
