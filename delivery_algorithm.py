from delivery_truck import Truck
import data_parser as data
import datetime

STARTING_HUB = 'Salt Lake City UT'


def deliver_all_packages(selection=None):
    """
    Runs the algorithm to deliver all packages. Starts by calling the load packages
    method. Then, while keeping track of the current time for each vehicle, delivers
    the packages in order, following special instructions using a greedy algorithm by
    heading to the closest stop first.
    :return:
    """
    truck_1 = Truck()
    truck_2 = Truck()
    last_loaded_index = 0
    status_checker_count = 0
    printed_morning, printed_afternoon, printed_evening = False, False, False

    # Set truck 2 start time to 0905 hrs to account for late packages.
    setattr(truck_2, "running_time", datetime.timedelta(hours=9, minutes=5))

    # print(f'TRUCK 1 STARTING TIME: {truck_1.running_time}')
    # print(f'TRUCK 2 STARTING TIME: {truck_2.running_time}\n')

    # Loads truck 1 and retains the last used index to make adding the remaining
    # packages faster by avoiding searching the entire hashtable every time. O(n).
    last_loaded_index += load_truck(truck_1, 1, last_loaded_index)

    # Start of day, set starting point to WGU.
    truck_1.current_location = STARTING_HUB
    truck_2.current_location = STARTING_HUB

    # This starts the main looping algorithm of the program to deliver all the
    # packages. The overall complexity of this algorithm is O(n^3) due to the linear
    # iteration through the package list, and the nested loops to determine the closest
    # stop for each truck as it delivers each package and moves the truck to the next
    # location.
    while truck_1.num_packages_loaded() > 0 \
            or truck_2.num_packages_loaded() > 0:

        # checks for the time to be within the window of the first package status check
        if datetime.timedelta(hours=8, minutes=35) < truck_1.running_time < \
                datetime.timedelta(hours=9, minutes=25) and not printed_morning:
            printed_morning = True  # determines if this report has already been ran

            if selection is None:  # the whole algorithm is ran all the reports will print
                display_all_packages_status('morning', truck_1.running_time)

            elif selection == 1:
                display_all_packages_status('morning', truck_1.running_time)
                return

        # checks for the time to be within the window of the second package status check
        elif datetime.timedelta(hours=9, minutes=35) < truck_1.running_time < \
                datetime.timedelta(hours=10, minutes=25) and not printed_afternoon:
            printed_afternoon = True

            if selection is None:
                display_all_packages_status('afternoon', truck_1.running_time)

            elif selection == 2:
                display_all_packages_status('afternoon', truck_1.running_time)
                return

        # get TRUCK 1 closest destination name, address, distance,
        # current location, and distance from that stop back to the hub
        if truck_1.num_packages_loaded() > 0:

            # print(f'\nFinding the next stop for TRUCK 1...')

            # uses the truck's current location and list of packages loaded to
            # determine the next stop
            truck_1_dest_name, truck_1_dest_address, truck_1_dest_distance, \
                truck_1_dest_hub_distance = \
                data.determine_next_stop(truck_1.current_location,
                                         truck_1.packages_loaded)

            # get truck travel time based on distance and truck speed
            truck_1_travel_mins, truck_1_travel_secs = \
                truck_1.calculate_time_traveled(truck_1_dest_distance)

            # adjust truck running time to add travel time to the next stop
            truck_1.track_time(truck_1_travel_mins, truck_1_travel_secs)

            # get delivery package ID to search with
            truck_1_current_package = data.hm.get_package_id(truck_1_dest_name)

            # mark as delivered and remove from TRUCK 1
            truck_1.deliver_package(truck_1_current_package,
                                    truck_1_dest_address,
                                    1, truck_1.running_time)

            # print(f'\tTime for Truck 1 to travel from {truck_1.current_location} '
            #       f'to {truck_1_dest_address} ({truck_1_dest_distance} miles) '
            #       f'is {truck_1_travel_mins} minutes and '
            #       f'{truck_1_travel_secs} seconds')
            # print(f'{truck_1.num_packages_loaded()} packages left on Truck 1')

            truck_1.total_miles_traveled += truck_1_dest_distance
            truck_1.current_location = truck_1_dest_address

        # If there are no more packages loaded, return truck to hub and add
        # miles and time traveled.
        elif truck_1.num_packages_loaded() == 0:
            # print(f'\n{"~" * 10} Truck 1 traveling back to hub for '
            #       f'{truck_1_dest_hub_distance} miles. {"~" * 10}')

            truck_1.total_miles_traveled += truck_1_dest_hub_distance
            truck_1_travel_mins, truck_1_travel_secs = \
                truck_1.calculate_time_traveled(truck_1_dest_hub_distance)

            # print(f'\tTime for Truck 1 to travel from'
            #       f' {truck_1.current_location} to '
            #       f'{STARTING_HUB} ({truck_1_dest_hub_distance} miles) '
            #       f'is {truck_1_travel_mins} minutes and '
            #       f'{truck_1_travel_secs} seconds\n')

            truck_1.current_location = STARTING_HUB
            truck_1.track_time(truck_1_travel_mins, truck_1_travel_secs)

            # Set time to 10:20 to simulate waiting for the correct address for
            # package 9 to reduce time complexity of looping through the remaining
            # packages every time a new destination needs to be selected.
            address_correction_time = datetime.timedelta(hours=10, minutes=20)

            if truck_1.running_time < address_correction_time:
                setattr(truck_1, 'running_time', address_correction_time)
            # reload truck 1 with the remaining packages for the day
            load_truck(truck_1, 1, last_loaded_index)

        # Load TRUCK 2 after algorithm time is past 9:05am to account for late packages.
        # Get closest destination name, address, distance, current location,
        # and distance from that stop back to the hub.
        if truck_1.running_time >= datetime.timedelta(hours=9, minutes=5):

            if status_checker_count == 0:
                status_checker_count = 1
                # print('\nTRUCK 2 IS NOW IN SERVICE')
                # print(f'Truck 2 left the depot at: {truck_2.running_time} hours')
                last_loaded_index += load_truck(truck_2, 2, last_loaded_index)

            if truck_2.num_packages_loaded() > 0:
                # print(f'\nFinding the next stop for TRUCK 2...')
                truck_2_dest_name, truck_2_dest_address, truck_2_dest_distance, \
                    truck_2_dest_hub_distance = \
                    data.determine_next_stop(truck_2.current_location,
                                             truck_2.packages_loaded)

                # Calculate time traveled based on the closest destination.
                truck_2_travel_mins, truck_2_travel_secs = \
                    truck_2.calculate_time_traveled(truck_2_dest_distance)

                # Add travel time to truck's current running time.
                truck_2.track_time(truck_2_travel_mins, truck_2_travel_secs)

                # Get delivery package ID.
                truck_2_current_package = data.hm.get_package_id(truck_2_dest_name)

                # Mark as delivered and remove from the truck.
                truck_2.deliver_package(truck_2_current_package,
                                        truck_2_dest_address,
                                        2, truck_2.running_time)

                # print(f'\tTime for Truck 2 to travel from {truck_2.current_location} '
                #       f'to {truck_2_dest_address} ({truck_2_dest_distance} miles) '
                #       f'is {truck_2_travel_mins} minutes and '
                #       f'{truck_2_travel_secs} seconds')
                # print(f'{truck_2.num_packages_loaded()} packages left on Truck 2')

                truck_2.total_miles_traveled += truck_2_dest_distance
                truck_2.current_location = truck_2_dest_address

                # If there are no more packages loaded, return truck to hub and add
                # miles and time traveled.
                if truck_2.num_packages_loaded() == 0 and status_checker_count == 1:
                    status_checker_count = 2
                    # print(f'\n{"~" * 10} Truck 2 traveling back to hub for '
                    #       f'{truck_2_dest_hub_distance} miles. {"~" * 10}')

                    truck_2.total_miles_traveled += truck_2_dest_hub_distance
                    truck_2_travel_mins, truck_2_travel_secs = \
                        truck_2.calculate_time_traveled(truck_2_dest_hub_distance)

                    # print(
                    #     f'\tTime for Truck 2 to travel from'
                    #     f' {truck_2.current_location} to '
                    #     f'{STARTING_HUB} ({truck_2_dest_hub_distance} miles) '
                    #     f'is {truck_2_travel_mins} minutes and '
                    #     f'{truck_2_travel_secs} seconds\n')

                    truck_2.current_location = STARTING_HUB

                    truck_2.track_time(truck_2_travel_mins, truck_2_travel_secs)

    # print(f'\n{"~" * 50} ALL PACKAGES DELIVERED {"~" * 50}\n')

    # The last time window for a package status check is after all the deliveries have
    # been made. This sets the time to within the required range and prints the package
    # status list.
    if data.hm.all_packages_loaded and truck_1.num_packages_loaded() == 0 and \
            truck_2.num_packages_loaded() == 0:
        last_report_window = datetime.timedelta(hours=13, minutes=0)

        if selection is None:
            display_all_packages_status('evening', last_report_window)

        elif selection == 3:
            display_all_packages_status('evening', last_report_window)
            return

    total_miles = truck_1.total_miles_traveled + truck_2.total_miles_traveled

    print(f"""
Truck 1 traveled {round(truck_1.total_miles_traveled, 2)} miles total.
Truck 1 returned to HUB at {truck_1.running_time}.
    
Truck 2 traveled {round(truck_2.total_miles_traveled, 2)} miles total.
Truck 2 returned to HUB at {truck_2.running_time}
    
For a total of {round(total_miles, 1)} miles between both trucks.
""")


def display_all_packages_status(time_period, time=None):
    """
    Takes time period and current time as input to display the status of all packages at
    a given time. O(n).
    :param time_period:
    :param time:
    :return:
    """
    if time_period == 'morning':
        print()
        data.print_line_break()
        print(f'DISPLAYING ALL PACKAGES for the time {time}. Falling between 8:35 and '
              f'9:25')
        data.print_line_break()

    elif time_period == 'afternoon':
        print()
        data.print_line_break()
        print(f'DISPLAYING ALL PACKAGES for the time {time}. Falling between 9:35 and '
              f'10:25')
        data.print_line_break()

    elif time_period == 'evening':
        print()
        data.print_line_break()
        print(f'DISPLAYING ALL PACKAGES for the time {time}. Falling between 12:03 and '
              f'13:12 (1:12 pm)')
        data.print_line_break()

    else:
        return

    # Iterate through entire hashtable to print all package's status. O(n).
    for item in data.hm:
        print(f'\t{item}')

    print()


def display_time_window(selection):
    """
    Prints the status of all packages within the user selected time window.
    :param selection:
    :return:
    """

    if selection == 1:
        deliver_all_packages(selection)
    elif selection == 2:
        deliver_all_packages(selection)
    elif selection == 3:
        deliver_all_packages(selection)
    else:
        print('Invalid selection.')
        return


def load_truck(truck, truck_num, starting_index):
    """
    Uses a truck object and truck number to load a truck with packages. Also track the
    last used index in the hashtable to avoid searching over a list of packages that has
    already been delivered.
    :param truck:
    :param truck_num:
    :param starting_index:
    :return:
    """
    index_counter = 0

    # Start at last loaded index to avoid looping through the entire hashtable every time.
    # Complexity is O(n) which will decrease with each subsequent search since you will
    # not have to look through the entire list each time to find a match.
    for x in range(starting_index, len(data.hm)):
        package = data.hm[x]
        package_id = package[0]
        package_special_note = package[1][5]
        package_delivery_status = package[1][6]

        if package_special_note != 'Wrong address listed' \
                and not package_delivery_status.__contains__('delivered'):

            if truck.num_packages_loaded() < 16:
                data.hm.set_delivery_status(package_id,
                                            f'Loaded on Truck {truck_num} '
                                            f'at {truck.running_time}')
                truck.load_package(package)
                index_counter += 1

            if truck.num_packages_loaded() == 16:
                break

        elif package_special_note == 'Wrong address listed':
            # checks for the time to be 10:20 which is when package #9 has it's address
            # information updated
            if truck.running_time >= datetime.timedelta(hours=10, minutes=20):
                data.hm.set_special_note(package_id,
                                         f'Address corrected at {truck.running_time}')
                data.hm.set_address(package_id, f'410 S State St')
                truck.load_package(package)
                index_counter += 1

    # Checks that the last item in the list of packages has been loaded onto the truck.
    if x == len(data.hm) - 1:
        setattr(data.hm, 'all_packages_loaded', 'True')

    return index_counter
