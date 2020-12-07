from delivery_truck import Truck
import data_parser as data
import datetime

STARTING_HUB = 'Salt Lake City UT'


def deliver_all_packages():
    """
    Runs the algorithm to deliver all packages. Starts by calling the `load packages`
    method. Then, while keeping track of the current time for each vehicle, delivers
    the packages in order, following special instructions using a greedy algorithm by
    heading to the closest stop first.
    :return:
    """
    list_of_stops = []
    truck_1 = Truck()
    truck_2 = Truck()

    # set truck 2 start time to 0905 hrs to account for late packages
    setattr(truck_2, "time", datetime.timedelta(hours=9, minutes=5))

    # create variables for truck 1 and truck 2 times
    truck_1_time = getattr(truck_1, "time")
    truck_2_time = getattr(truck_2, "time")

    print(f'TRUCK 1 STARTING TIME: {truck_1_time}')
    print(f'TRUCK 2 STARTING TIME: {truck_2_time}\n')

    # loop to load initial set of packages to start the day
    # and find the first stop to be made based on distance
    for package in data.hm:
        package_id = package[0]
        package_special_note = package[1][5]

        if package_special_note != 'Wrong address listed':
            if truck_1.num_packages_loaded() < 16 \
                    and package_special_note != 'Can only be on truck 2':
                data.hm.set_delivery_status(package_id, 'Loaded on Truck 1')
                truck_1.load_package(package)
                list_of_stops.append(package)

            elif truck_2.num_packages_loaded() < 16 \
                    and package_special_note != 'Can only be on truck 1':
                data.hm.set_delivery_status(package_id, 'Loaded on Truck 2')
                truck_2.load_package(package)
                list_of_stops.append(package)

        # list of all stops between both trucks
    # for x in list_of_stops:
    #     print(f'LOADED: {x}')
    # start of day, set starting point to WGU
    truck_1.current_location = STARTING_HUB
    truck_2.current_location = STARTING_HUB

    while truck_1.num_packages_loaded() > 0 \
            and truck_2.num_packages_loaded() > 0:

        print(f'\n\tTruck 1 current location: {truck_1.current_location}')
        print(f'\tNumber of packages left on truck 1:'
              f' {truck_1.num_packages_loaded()}')

        print(f'\n\tTruck 2 current location: {truck_2.current_location}')
        print(f'\tNumber of packages left on truck 1:'
              f' {truck_2.num_packages_loaded()}')

        # get TRUCK 1 closest destination name, address, distance,
        # current location, and distance from that stop back to the hub
        print(f'\n{"*" * 10} Finding the next stop for TRUCK 1 {"*" * 10}', end='')
        truck_1_dest_name, truck_1_dest_address, truck_1_dest_distance, \
            truck_1_dest_hub_distance = \
            data.determine_next_stop(truck_1.current_location,
                                     truck_1.packages_loaded)

        # get TRUCK 2 closest destination name, address, distance,
        # current location, and distance from that stop back to the hub
        print(f'\n{"*" * 10} Finding the next stop for TRUCK 2 {"*" * 10}', end='')
        truck_2_dest_name, truck_2_dest_address, truck_2_dest_distance, \
            truck_2_dest_hub_distance = \
            data.determine_next_stop(truck_2.current_location,
                                     truck_2.packages_loaded)

        # get delivery package ID
        truck_1_current_package = data.hm.get_package_id(truck_1_dest_name)
        truck_2_current_package = data.hm.get_package_id(truck_2_dest_name)

        # mark as delivered and remove from TRUCK 1 and TRUCK 2
        truck_1.deliver_package(truck_1_current_package, truck_1_dest_address)
        truck_2.deliver_package(truck_2_current_package, truck_2_dest_address)

        truck_1_travel_mins, truck_1_travel_secs = \
            truck_1.calculate_time_traveled(truck_1_dest_distance)

        print(f'\tTime for Truck 1 to travel from {truck_1.current_location} '
              f'to {truck_1_dest_address} ({truck_1_dest_distance} miles) '
              f'is {truck_1_travel_mins} minutes and '
              f'{truck_1_travel_secs} seconds')

        truck_1_time += datetime.timedelta(
            minutes=truck_1_travel_mins,
            seconds=truck_1_travel_secs)

        print(f'\tTruck 1\'s package delivered at {truck_1_time}\n')

        truck_1.miles_traveled += truck_1_dest_distance
        truck_1.current_location = truck_1_dest_address

        # mark as delivered and remove from TRUCK 2
        truck_2_travel_mins, truck_2_travel_secs = \
            truck_2.calculate_time_traveled(truck_2_dest_distance)

        print(f'\tTime for Truck 2 to travel from {truck_2.current_location} '
              f'to {truck_2_dest_address} ({truck_2_dest_distance} miles) '
              f'is {truck_2_travel_mins} minutes and '
              f'{truck_2_travel_secs} seconds')

        truck_2_time += datetime.timedelta(
            minutes=truck_2_travel_mins,
            seconds=truck_2_travel_secs)

        print(f'\tTruck 2\'s package delivered at {truck_2_time}\n')

        truck_2.miles_traveled += truck_2_dest_distance
        truck_2.current_location = truck_2_dest_address

        # if there are no more packages loaded, return TRUCK 1 to hub and add
        # miles and time traveled
        if truck_1.num_packages_loaded() == 0:
            print(f'\n{"~" * 10} Truck 1 traveling back to hub for '
                  f'{truck_1_dest_hub_distance} miles. {"~" * 10}')

            truck_1.miles_traveled += truck_1_dest_hub_distance
            truck_1_travel_mins, truck_1_travel_secs = \
                truck_1.calculate_time_traveled(truck_1_dest_hub_distance)

            print(f'\nTime for Truck 1 to travel from'
                  f' {truck_1.current_location} to '
                  f'{STARTING_HUB} ({truck_1_dest_hub_distance} miles) '
                  f'is {truck_1_travel_mins} minutes and '
                  f'{truck_1_travel_secs} seconds\n')

            truck_1.current_location = STARTING_HUB

            truck_1_time += datetime.timedelta(
                minutes=truck_1_travel_mins,
                seconds=truck_1_travel_secs)

        # if there are no more packages loaded, return TRUCK 2 to hub and add
        # miles and time traveled
        if truck_2.num_packages_loaded() == 0:
            print(f'\n{"~" * 10} Truck 2 traveling back to hub for '
                  f'{truck_2_dest_hub_distance} miles. {"~" * 10}')

            truck_2.miles_traveled += truck_2_dest_hub_distance
            truck_2_travel_mins, truck_2_travel_secs = \
                truck_2.calculate_time_traveled(truck_2_dest_hub_distance)

            print(
                f'\nTime for Truck 2 to travel from'
                f' {truck_2.current_location} to '
                f'{STARTING_HUB} ({truck_2_dest_hub_distance} miles) '
                f'is {truck_2_travel_mins} minutes and '
                f'{truck_2_travel_secs} seconds\n')

            truck_2.current_location = STARTING_HUB

            truck_2_time += datetime.timedelta(
                minutes=truck_2_travel_mins,
                seconds=truck_2_travel_secs)

        # remove stop from list of packages that need to be delivered if it is
        # a package in either TRUCK 1 or TRUCK 2
        for stop in list_of_stops:
            if stop[1][0] == truck_1_dest_address or \
                    stop[1][0] == truck_2_dest_address:
                list_of_stops.remove(stop)

    print(f'{"~" * 25} ALL PACKAGES DELIVERED {"~" * 25}')

    # return truck to hub for more packages
    print(f'\n\tTruck 1 traveled '
          f'{round(truck_1.miles_traveled, 2)} miles total.')
    print(f'\tTruck 1 returned to HUB at {truck_1_time}')

    print(f'\n\tTruck 2 traveled '
          f'{round(truck_2.miles_traveled, 2)} miles total.')
    print(f'\tTruck 1 returned to HUB at {truck_2_time}')
