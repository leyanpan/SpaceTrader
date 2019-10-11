from enum import Enum
import numpy as np
from region import Region
from universe import Universe
from settings import SQUARE_SIDE_MAX, LISTOFNAMES, REGION_NUM, MAX_FUEL
from ship import Ship
from player import Player


class Game:
    __instance = None
    @staticmethod
    def get_instance():
        if Game.__instance is None:
            return None
        return Game.__instance

    def __init__(self, game_difficulty, name, skills):
        if Game.__instance is not None:
            raise Exception('Game instance already exists')
        self.game_difficulty = game_difficulty
        self.difficulty_multiplier = self.game_difficulty.value
        self.player = None
        self.universe = None
        self.name_region = None
        self.start_game(name, skills)
        Game.__instance = self

    @staticmethod
    def remove_instance():
        Game.__instance = None
        Universe.remove_instance()

    def start_game(self, name, skills):
        names = np.random.choice(LISTOFNAMES, size=10, replace=False)
        x_s = Game.generate_random_sequence(REGION_NUM)
        y_s = Game.generate_random_sequence(REGION_NUM)
        regions = []
        self.name_region = {}
        for i in range(10):
            self.name_region[names[i]] = Region((x_s[i], y_s[i]), names[i])
            regions.append(self.name_region[names[i]])
        self.universe = Universe(regions)
        ship = Ship(np.random.choice(self.universe.regions), MAX_FUEL)
        self.player = Player(name, skills, ship)

    @staticmethod
    def generate_random_sequence(num):
        rand_list = []
        while len(rand_list) < num:
            rand_int = np.random.randint(-SQUARE_SIDE_MAX, SQUARE_SIDE_MAX)
            valid = True
            for prev in rand_list:
                if np.abs(prev - rand_int) <= 5:
                    valid = False
            if valid:
                rand_list.append(rand_int)
        return rand_list

    def get_all_possible_travel_region(self):
        current_region = self.player.region
        possible_regions = []
        for region in self.universe.regions:
            if region is not current_region:
                possible_regions.append(region)
        return possible_regions

    def calculate_cost_to(self, region):
        return self.player.region.calculate_distance(region) * self.difficulty_multiplier

    @property
    def current_region_num(self):
        return self.universe.regions.index(self.player.region)

    def travel_to_region_string(self, region):
        self.player.travel_to_region(self.name_region[region])


class DifficultyEnum(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3
