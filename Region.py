from enum import Enum
import numpy as np
class Region:
    def __init__(self, tech_level, coordinates, name):
        self.techLevel = tech_level
        self.coordinates = coordinates
        self.name = name

    def calculate_distnace(self, other_region):
        other_coordinates = other_region.coordinates
        return np.sqrt((self.coordinates[0] - other_coordinates[0]) ** 2 + (self.coordinates[1] - other_coordinates[1]) ** 2)


class TechLevel(Enum):
    PRE_AG = 0
    AGRICULTURE = 1
    MEDIEVAL = 2
    RENAISSANCE = 3
    INDUSTRIAL = 4
    MODERN = 5
    FUTURISTIC = 6