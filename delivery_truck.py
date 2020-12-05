from data_parser import hm

class Truck:

    def __init__(self):
        self.packages_loaded = []  # list of packages currently on the truck
        self.hubs_visited = []
        self.TRUCK_SPEED = 18  # static truck speed is 18 mph
        self.current_location = ''
        self.destination = ''
        self.miles_traveled = 0

    def load_package(self, package):
        """
        Appends packages to the list of packages that are currently on the
        truck to be delivered
        :param package:
        :return:
        """
        self.packages_loaded.append(package)

    def deliver_package(self, package_id):
        """
        Finds package on the truck and "delivers" it by removing it from the
        list of packages currently on the truck and marking it as delivered
        in the hashmap.
        :param package_id:
        :return: none
        """
        # print('packages on truck before delivery')
        # for x in self.packages_loaded:
        #     print('\t', x)

        for x, package in enumerate(self.packages_loaded):
            if package[0] == package_id:
                self.packages_loaded.remove(package)
                hm.set_delivery_status(package_id, 'Delivered')

                # for z in hm:
                #     print(z)

                # print('\npackages on truck after delivery')
                # for y in self.packages_loaded:
                #     print('\t', y)

                return

    def num_packages_loaded(self):
        """
        Returns number of packages currently on the truck.
        :return:
        """
        return len(self.packages_loaded)

    def calculate_time_traveled(self, distance):
        """
        Gets travel time in minutes
        Takes distance divided by the constant truck speed which gives time in
        a fraction of an hour. Then multiplies by 60 to get the time in minutes
        rounded to 2 decimal places.
        :param distance: miles to the destination
        :return: travel time in minutes
        """
        travel_time = (distance / self.TRUCK_SPEED) * 60
        return round(travel_time, 2)
