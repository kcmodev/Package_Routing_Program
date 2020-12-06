from delivery_truck import Truck
import data_parser as data
import datetime

STARTING_HUB = 'Salt Lake City UT'

truck_1 = Truck()
truck_2 = Truck()


def deliver_all_packages():
    list_of_stops = []
    # sets starting time to 0800 for the first delivery
    algorithm_time = datetime.datetime(2020, 12, 6, 8, 0, 0)

    print(f'STARTING TIME: {algorithm_time.time()}')

    # loop to load initial set of packages to start the day
    # and find the first stop to be made based on distance
    for package in data.hm:
        # if truck_1.num_packages_loaded() < 16:
        if truck_1.num_packages_loaded() < 3:
            truck_1.load_package(package)

        elif truck_2.num_packages_loaded() < 3:
            truck_2.load_package(package)

        # list of all stops between both trucks
        list_of_stops.append(package)
        print(f'LOADED: {package}')

    # start of day, set starting point to WGU
    truck_1.current_location = STARTING_HUB

    while truck_1.num_packages_loaded() > 0:
        print(f'\nTruck 1 current location: {truck_1.current_location}')
        print(f'Number of packages left on truck 1:'
              f' {truck_1.num_packages_loaded()}')

        # get truck 1 closest destination name, address, distance,
        # current location, and distance from that stop back to the hub
        next_stop_name, next_stop_address, next_stop_distance, \
            next_stop_hub_distance = \
            data.determine_next_stop(truck_1.current_location, list_of_stops)

        # get delivery package ID
        delivered_package_id = data.hm.get_package_id(next_stop_name)

        # mark as delivered and remove from truck
        truck_1.deliver_package(delivered_package_id)

        travel_time_minutes, travel_time_seconds = \
            truck_1.calculate_time_traveled(next_stop_distance)

        print(f'Time for Truck 1 to travel from {truck_1.current_location} to '
              f'{next_stop_address} ({next_stop_distance} miles) '
              f'is {travel_time_minutes} minutes and '
              f'{travel_time_seconds} seconds')

        algorithm_time += datetime.timedelta(
            minutes=travel_time_minutes,
            seconds=travel_time_seconds)

        truck_1.miles_traveled += next_stop_distance
        truck_1.current_location = next_stop_address

        # if there are no more packages loaded, return truck to hub and add
        # miles and time traveled
        if truck_1.num_packages_loaded() == 0:
            print(f'\n{"~" * 10} Truck 1 traveling back to hub for '
                  f'{next_stop_hub_distance} miles. {"~" * 10}')

            truck_1.miles_traveled += next_stop_hub_distance
            travel_time_minutes, travel_time_seconds = \
                truck_1.calculate_time_traveled(next_stop_hub_distance)

            print(
                f'\nTime for Truck 1 to travel from'
                f' {truck_1.current_location} to '
                f'{STARTING_HUB} ({next_stop_hub_distance} miles) '
                f'is {travel_time_minutes} minutes and '
                f'{travel_time_seconds} seconds\n')

            truck_1.current_location = STARTING_HUB

            algorithm_time += datetime.timedelta(
                minutes=travel_time_minutes,
                seconds=travel_time_seconds)

        # remove stop from list of packages that need to be delivered
        for stop in list_of_stops:
            if stop[1][0] == next_stop_address:
                list_of_stops.remove(stop)
                break

    print('ALL PACKAGES DELIVERED')

    # return truck to hub for more packages
    print(f'\nTruck 1 traveled '
          f'{round(truck_1.miles_traveled, 2)} miles total.')
    print(f'Truck 1 returned to HUB at {algorithm_time.time()}')
