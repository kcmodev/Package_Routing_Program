class Truck:

    def __init__(self):
        self.packages_loaded = []  # list of packages currently on the truck
        self.hubs_visited = []
        self.speed = 18  # static truck speed is 18 mph
        self.current_location = ''
        self.destination = ''

    def load_packages(self, package):
        self.packages_loaded.append(package)

    def travel(self):
        pass
