from parcel_delivery import Truck
import data_parser as data

STARTING_HUB = 'Salt Lake City UT'

truck_1 = Truck()
# truck_2 = Truck()


def deliver_packages():
    list_of_stops = []

    # loop to load initial set of packages to start the day
    # and find the first stop to be made based on distance
    for package in data.hm:
        truck_1.load_packages(package)
        list_of_stops.append(package[1][0])  # package destination address
        print(f'LOADED: {package}')

    # start of day, set starting point to WGU
    # truck_1.current_location = data.stops.get(STARTING_HUB)
    truck_1.__setattr__('current_location', STARTING_HUB)
    print(f'truck 1 current loc: {truck_1.current_location}')
    data.determine_next_stop(STARTING_HUB, list_of_stops)


def find_next_stop():

    for package in truck_1.packages_loaded:
        pass
