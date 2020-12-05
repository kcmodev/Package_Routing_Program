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
        list_of_stops.append(package)  # package destination address
        print(f'LOADED: {package}')

    # start of day, set starting point to WGU
    truck_1.current_location = STARTING_HUB
    # truck_1.__setattr__('current_location', STARTING_HUB)
    print(f'Truck 1 current location: {truck_1.current_location}')

    while truck_1.num_packages_loaded() > 0:
        print(f'num pkgs loaded: {truck_1.num_packages_loaded()}')
        # get the closest stop
        next_stop_name, next_stop_address, next_stop_distance = \
            data.determine_next_stop(truck_1.current_location, list_of_stops)

        # get delivery package ID
        delivered_package_id = data.hm.get_package_id(next_stop_name)

        # mark as delivered and remove from truck
        truck_1.deliver_package(delivered_package_id)
        truck_1.current_location = next_stop_address

        # remove stop from list of packages that need to be delivered
        for stop in list_of_stops:
            if stop[1][0] == next_stop_address:
                list_of_stops.remove(stop)
                break

        # print('\nlist_of_stops[] (in main algo) after a delete:')
        # for x in list_of_stops:
        #     print('\t', x)

    print('ALL PACKAGES DELIVERED')


def find_next_stop():
    for package in truck_1.packages_loaded:
        pass
