class Truck:

    def __init__(self):
        self.packages_loaded = []  # list of packages currently on the truck
        self.hubs_visited = []
        self.TRUCK_SPEED = 18  # static truck speed is 18 mph
        self.current_location = ''
        self.destination = ''
        self.miles_traveled = 0

    def load_package(self, package):
        self.packages_loaded.append(package)

    def travel(self):
        pass

    def deliver_package(self, package_id):
        print('packages on truck before delivery')
        for x in self.packages_loaded:
            print('\t', x)

        for x, package in enumerate(self.packages_loaded):
            if package[0] == package_id:
                self.packages_loaded.remove(package)

                print('\npackages on truck after delivery')
                for y in self.packages_loaded:
                    print('\t', y)

                return

    def calculate_miles_traveled(self):
        pass
