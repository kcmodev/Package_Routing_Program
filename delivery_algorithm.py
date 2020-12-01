from delivery_truck import Truck
import data_parser as data

STARTING_HUB = 'Salt Lake City UT'

truck_1 = Truck()
# truck_2 = Truck()


def deliver_all_packages():
    list_of_stops = []

    # loop to load initial set of packages to start the day
    # and find the first stop to be made based on distance
    for package in data.hm:
        truck_1.load_package(package)
        list_of_stops.append(package[1][0])  # package destination address
        print(f'LOADED: {package}')

    # start of day, set starting point to WGU
    # truck_1.current_location = data.stops.get(STARTING_HUB)
    truck_1.__setattr__('current_location', STARTING_HUB)
    print(f'Truck 1 current location: {truck_1.current_location}')

    for package in truck_1.packages_loaded:
        # get the closest stop
        next_stop_name = data.determine_next_stop(STARTING_HUB, list_of_stops)

        # get delivery package ID
        delivered_package_id = data.hm.get_package_id(next_stop_name)

        # mark as delivered and remove from truck
        truck_1.deliver_package(delivered_package_id)

        # remove stop from list of packages that need to be delivered
        # list_of_stops.pop(next(x for x in list_of_stops if
        #                        x.__getattribute__('address')
        #                        == next_stop_name))


def find_next_stop():

    for package in truck_1.packages_loaded:
        pass
