from enum import Enum
import random
import numpy as np

class Region:
    def __init__(self, coordinates, name):
        self.tech_level = random.choice(list(TechLevel))
        self.coordinates = coordinates
        self.name = name
        self.image_url = "/static/images_regions/" + name.replace(' ', '') + ".JPG"

    def calculate_distance(self, other_region):
        other_coordinates = other_region.coordinates
        return np.sqrt((self.coordinates[0] - other_coordinates[0]) ** 2 +
                       (self.coordinates[1] - other_coordinates[1]) ** 2)

    def get_name(self):
        return self.name


class TechLevel(Enum):
    PRE_AG = 0
    AGRICULTURE = 1
    MEDIEVAL = 2
    RENAISSANCE = 3
    INDUSTRIAL = 4
    MODERN = 5
    FUTURISTIC = 6
