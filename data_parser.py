import csv
from hashmap import HashMap

hm = HashMap()
stops = {}
names_and_addresses = {}


def parse_distance_table():
    """
    Parses csv file `Distance Table` and fills a list with the data. Uses
    `package id` as the index for the list to make searching O(1)
    :return: None. Fills list with parsed data.
    """

    # add all lines as a list to be enumerated and added to a dictionary in
    # the next step
    print('Distance table loaded and parsed....')
    with open('data/Distance Table.csv') as distance_table:
        distances = [row for row in csv.reader(distance_table)]

    # iterates over csv file and adds each stop name value from each row[0]
    # as the key. Then adds the dict values as a list of destination and
    # distance pair for a time complexity of O(n^2)

    # iterate over columns
    for x in range(0, len(distances)):
        stops_list = []
        if x > 0:  # puts first line at WGU in the csv file column header
            start_name = str(distances[x][0]).strip()
            start_address = str(distances[x][1])[0:-8]
            start_address.strip()

            # makes an associative list between stop names and addresses
            names_and_addresses[start_address] = start_name
            # iterate down rows
            for y in range(0, len(distances[x])):
                if y > 1:
                    stop_name = distances[0][y]
                    stop_distance = distances[x][y]

                    # append the values to the list
                    stops_list.append([stop_distance.strip(),
                                       stop_name.strip()])

            # assign a dictionary key to the values in the form
            # of the stop name
            stops[f'{start_name}'] = stops_list


def determine_distance(start_address, stop_address):
    distance, back_to_hub = 0.0, 0.0

    # use stop name as key
    # search list of stops for corresponding value
    origination_name = names_and_addresses.get(start_address)
    destination_name = names_and_addresses.get(stop_address)

    origination_index = list(names_and_addresses.keys()).index(start_address)
    destination_index = list(names_and_addresses.keys()).index(stop_address)

    origination_distance_list = stops[origination_name]
    destination_distance_list = stops[destination_name]

    # check where address falls in the list
    # if stop is after, use stop location to find distance

    if origination_index < destination_index:
        # use list of stops distance associated with the destination
        # return distance to destination from destination list

        for stop in destination_distance_list:
            if stop[1] == origination_name:
                distance = float(stop[0])
                # saves distance from destination to hub
                back_to_hub = float(destination_distance_list[0][0])
                break

    # if the start is before, then use start location to determine the distance
    elif origination_index > destination_index:
        # get list of stops distance associated with the trip origination
        # return distance to destination from origination list

        for stop in origination_distance_list:
            if stop[1] == destination_name:
                distance = float(stop[0])
                back_to_hub = float(destination_distance_list[0][0])
                break

    return distance, destination_name, back_to_hub


def determine_next_stop(start, list_of_stops):
    print(f'\n{"*" * 10} finding stop closest to {start} {"*" * 10}')
    closest_stop_distance = 99999
    closest_stop_hub_distance = 0.0
    closest_stop_name, closest_stop_address = '', ''

    for x, stop in enumerate(list_of_stops):
        distance, stop_name, back_to_hub = determine_distance(start,
                                                              stop[1][0])
        print(f'\t{stop_name} is {distance} miles away.')

        if distance < closest_stop_distance and distance != 0.0:
            closest_stop_distance = distance
            closest_stop_name = stop_name
            closest_stop_address = stop[1][0]
            closest_stop_hub_distance = back_to_hub

    print(f'\n\tShortest distance: {closest_stop_distance} miles. '
          f'Next stop is: {closest_stop_name} ({closest_stop_address}).\n')

    return closest_stop_name, closest_stop_address, closest_stop_distance, \
        closest_stop_hub_distance


def parse_package_file(package_file):
    """
    Parses csv file `Package File` and fills a list with the data. Uses
    `package id` as the index for the list to make searching O(1)
    :return: None. Fills list with parsed data.
    """

    print('Package file loaded and parsed....')
    with open(package_file) as distance_table:
        lines = csv.reader(distance_table)

        # enumerate and fill package data O(n)
        for x, line in enumerate(lines):
            if x != 0:
                # packages.append(line)
                package_id = line[0]
                address = line[1]
                city = line[2]
                state = line[3]
                zipcode = line[4]
                deadline = line[5]
                weight = line[6]

                if 7 < len(line) < 9:
                    note = line[7]
                else:
                    note = None

                hm.__setitem__(package_id, address, deadline, city, zipcode,
                               weight, note)

    # for package in hm:
    #     print(package)


def package_search(package_id: int):
    """
    Takes in package ID and returns all package data.
    :param package_id:
    :return: Package information
    """
    try:
        if package_id > 0:
            if package_id - 1 < len(hm):
                print_line_break()
                print()
                print(f'Package ID #{package_id} information:\n')
                print(hm.__getitem__(package_id - 1))
                print()
            else:
                raise ValueError
        else:
            raise ValueError

    except ValueError:
        print(f'"{package_id}" is not a valid selection.')


def get_address_from_name(address):
    for key, value in names_and_addresses.items():
        if value == address:
            return key


def print_line_break():
    print('*' * 100)
