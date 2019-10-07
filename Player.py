class Player:
    def __init__(self, name, skills, ship):
        self.name = name
        self.skills = skills
        self.ship = ship

    @property
    def region(self):
        return self.ship.region

    def travel_to_region(self, region):
        # TODO: Check is fuel is enough in further interations
        self.ship.travel_to_region(region)