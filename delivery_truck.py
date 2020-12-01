class Truck:

    def __init__(self):
        self.packages_loaded = []  # list of packages currently on the truck
        self.hubs_visited = []
        self.speed = 18  # static truck speed is 18 mph
        self.current_location = ''
        self.destination = ''
        self.miles_traveled = 0

    def load_package(self, package):
        self.packages_loaded.append(package)

    def travel(self):
        pass

    def deliver_package(self, package_id):
        # self.packages_loaded.pop()
        print('packages before')
        for x in self.packages_loaded:
            print('\t', x)

        for x, package in enumerate(self.packages_loaded):
            if package[0] == package_id:
                del self.packages_loaded[x]
                print('packages after')
                for x in self.packages_loaded:
                    print('\t', x)
                return



    def calculate_miles_traveled(self):
        pass
