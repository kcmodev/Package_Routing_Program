import csv

from hash_table import HashTable

hm = HashTable()
all_destinations = {}
names_and_addresses = {}


def determine_distance(origination_address, destination_address):
    """
    Uses the origination and destination addresses to determine the shortest stop relative
    to the truck's current location. O(n).
    :param origination_address:
    :param destination_address:
    :return:
    """
    distance, back_to_hub = 0.0, 0.0

    # Retrieve values of keys for corresponding destination addresses O(1).
    origination_name = names_and_addresses.get(origination_address)
    destination_name = names_and_addresses.get(destination_address)

    # Retrieve the index of each name to determine how to search the distance table O(n).
    origination_index = list(names_and_addresses.keys()).index(origination_address)
    destination_index = list(names_and_addresses.keys()).index(destination_address)

    # Retrieve the respective distance table lines from the stops dict O(1).
    origination_distance_list = all_destinations[origination_name]
    destination_distance_list = all_destinations[destination_name]

    # Check where address falls in the list.
    # If destination is after, use destination location to find the travel distance.
    if origination_index < destination_index:

        # Return distance to destination from destination list.
        # Breaks after a match is found to avoid searching the entire list unless
        # necessary. O(n).
        for stop in destination_distance_list:
            if stop[1] == origination_name:
                distance = float(stop[0])
                # Saves distance from destination to hub for the end of the route.
                back_to_hub = float(destination_distance_list[0][0])
                break

    # If the destination is before origination in the distance table
    # then use origination location to determine the distance.
    elif origination_index > destination_index:

        # Return distance to destination from origination list.
        # Breaks after a match is found to avoid searching the entire list unless
        # necessary. O(n).
        for stop in origination_distance_list:
            if stop[1] == destination_name:
                distance = float(stop[0])
                # Saves distance from destination to hub.
                back_to_hub = float(destination_distance_list[0][0])
                break

    return distance, destination_name, back_to_hub


def determine_next_stop(start, all_packages_loaded):
    """
    Determines the trucks closest stop and returns the result as the truck's next stop.
    :param start:
    :param all_packages_loaded:
    :return:
    """
    closest_stop_distance = 99999
    closest_stop_hub_distance = 0.0
    closest_stop_name, closest_stop_address = '', ''

    # Iterate through the packages on the truck and determine the destination
    # closest to the origination. O(n^2).
    for package in all_packages_loaded:
        distance, stop_name, back_to_hub = determine_distance(start,
                                                              package[1][0])

        # When shortest distance is found; save distance, name, address. Distance back to
        # hub saved to be used the end of the route is reached.
        if distance < closest_stop_distance and distance != 0.0:
            closest_stop_distance = distance
            closest_stop_name = stop_name
            closest_stop_address = package[1][0]
            closest_stop_hub_distance = back_to_hub

    # print(f'\tShortest distance: {closest_stop_distance} miles. '
    #       f'Next stop is: {closest_stop_name} ({closest_stop_address}).')

    return closest_stop_name, closest_stop_address, closest_stop_distance, \
        closest_stop_hub_distance


def get_address_from_name(address):
    """
    Takes in the name of the location and returns the address. O(n) worst case. Will
    break out if it finds the address early.
    :param address:
    :return:
    """
    for key, value in names_and_addresses.items():
        if value == address:
            return key


def package_search(package_id):
    """
    Searches hashtable by package id and returns the appropriate package.
    :param package_id:
    :return:
    """

    for package in hm:
        if package[0] == package_id:
            print(package)
            return

    print('No package with that ID found.')
    return

def parse_package_file(package_file):
    """
    Parses csv file `Package File` and fills a list with the data. Uses
    `package id` as the index for the list to make searching O(1)
    :return: None. Fills list with parsed data.
    """

    print('Package file loaded and parsed....')
    with open(package_file) as distance_table:
        lines = csv.reader(distance_table)

        # Enumerate and fill package data O(n).
        for x, line in enumerate(lines):
            if x != 0:  # Does not add first line (column titles).
                package_id = int(line[0])
                address = line[1]
                city = line[2]
                zipcode = line[4]
                deadline = line[5]
                weight = line[6]

                if 7 < len(line) < 9:
                    note = line[7]
                else:
                    note = None

                hm.__setitem__(package_id, address, deadline, city, zipcode,
                               weight, note)


def parse_distance_table():
    """
    Parses csv file `Distance Table` and fills a list with the data. Uses
    `package id` as the index for the list to make searching O(1)
    :return: None. Fills list with parsed data.
    """

    # Add all lines as a list to be enumerated and added to a dictionary in
    # the next step.
    print('Distance table loaded and parsed....')

    with open('data/Distance Table.csv') as distance_table:
        distances = [row for row in csv.reader(distance_table)]

    # Iterates over csv file and adds each stop name value from each row[0]
    # as the key. Then adds the dict values as a list of destination and
    # distance pair. O(n^2).
    for x in range(0, len(distances)):  # Iterate over columns.
        stops_list = []
        if x > 0:  # Puts first line at WGU in the csv file column header.
            origination_name = str(distances[x][0]).strip()
            origination_address = str(distances[x][1])[0:-8]
            origination_address.strip()

            # Builds an associative list between stop names and addresses.
            names_and_addresses[origination_address] = origination_name

            for y in range(0, len(distances[x])):  # iterate down rows
                if y > 1:
                    destination_name = distances[0][y]
                    destination_distance = distances[x][y]

                    # Append the values to the list.
                    stops_list.append([destination_distance.strip(),
                                       destination_name.strip()])

            # Assign a dictionary key to the values in the form of the stop name
            all_destinations[f'{origination_name}'] = stops_list


def print_line_break():
    """
    User for formatting and readability.
    :return:
    """
    print('*' * 100)
