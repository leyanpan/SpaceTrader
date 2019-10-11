class Universe:
    __instance = None
    @staticmethod
    def get_instance():
        return Universe.__instance

    def __init__(self, regions):
        if Universe.__instance is not None:
            raise Exception("creating a second instance")
        else:
            Universe.__instance = self
        self.regions = regions

    def get_all_regions(self):
        return self.regions

    @staticmethod
    def remove_instance():
        Universe.__instance = None
