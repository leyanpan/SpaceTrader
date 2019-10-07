from enum import Enum
from Region import Region, TechLevel
import numpy as np
from Universe import Universe
from settings import SQUARE_SIDE_MAX, LISTOFNAMES, REGION_NUM, MAX_FUEL
from Ship import Ship
from Player import Player


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
        self.start_game(name, skills)
        Game.__instance = self

    def start_game(self, name, skills):
        names = np.random.choice(LISTOFNAMES, size=10, replace=False)
        xs = Game.generate_random_sequence(REGION_NUM)
        ys = Game.generate_random_sequence(REGION_NUM)
        regions = []
        for i in range(10):
            regions.append(Region(np.random.choice(list(TechLevel)), (xs[i], ys[i]), names[i]))
        self.universe = Universe(regions)
        ship = Ship(np.random.choice(self.universe.regions), MAX_FUEL)
        self.player = Player(name, skills, ship)

    @staticmethod
    def generate_random_sequence(n):
        rand_list = []
        while len(rand_list) < n:
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
            if not region is current_region:
                possible_regions.append(region)
        return possible_regions

    def calculate_cost_to(self, region):
        return self.player.region.calculate_distnace(region) * self.difficulty_multiplier


class DifficultyEnum(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3