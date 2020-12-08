import datetime

from data_parser import hm


class Truck:
    """
    Truck object to track packages on the truck, as well as calculate speed
    and distance traveled.
    """

    def __init__(self):
        self.packages_loaded = []  # list of packages currently on the truck
        self.hubs_visited = []
        self.TRUCK_SPEED = 18  # static truck speed is 18 mph
        self.current_location = ''
        self.destination = ''
        self.miles_traveled = 0
        self.running_time = datetime.timedelta(hours=8, minutes=0, seconds=0)

    def load_package(self, package):
        """
        Appends packages to the list of packages that are currently on the
        truck to be delivered
        :param package:
        :return:
        """
        self.packages_loaded.append(package)

    def deliver_package(self, package_id, package_address, truck_num, delivery_time):
        """
        Finds package on the truck and "delivers" it by removing it from the
        list of packages currently on the truck and marking it as delivered
        in the hashmap.
        :param delivery_time:
        :param truck_num:
        :param package_address:
        :param package_id:
        :return: none
        """

        # this has to run in reverse to avoid erroneous results resulting from
        # altering the index of the list while iterating in the normal fashion
        for package in reversed(self.packages_loaded):
            if package[0] == package_id or package[1][0] == package_address:
                self.packages_loaded.remove(package)
                hm.set_delivery_status(package[0], f'Delivered by Truck {truck_num} at '
                                                   f'{delivery_time}')

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
        and then 60 again for seconds. Rounded up.
        :param distance: miles to the destination
        :return: travel time in minutes
        """
        travel_time = (distance / self.TRUCK_SPEED) * 60 * 60
        travel_minutes = int(travel_time / 60)
        travel_seconds = int(travel_time % 60)

        return travel_minutes, travel_seconds

    def track_time(self, travel_mins, travel_secs):
        self.running_time += datetime.timedelta(minutes=travel_mins, seconds=travel_secs)
