import csv
import re
from hashmap import HashMap
from collections import defaultdict

hm = HashMap()
# stops = defaultdict(list)
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
        # lines = csv.reader(distance_table)
        distances = [row for row in csv.reader(distance_table)]

    # iterates over csv file and adds each stop name value from each row[0]
    # as the key. Then adds the dict values as a list of destination and
    # distance pair for a time complexity of O(n^2)
    # for x, row in enumerate(distances):
    #     stop_list = []
    #     if x > 0:  # skips first row
    #         for y, col in enumerate(row):  # iterates over the columns
    #             if 1 < y < len(row):
    #                 # assigns the miles column w/ the destination
    #                 # skipping the first stop which is 'HUB'
    #                 if row[0] == 'Western Governors University' \
    #                         and distances[x][y] == '0.0':
    #                     continue
    #                 else:
    #                     stop_list.append((distances[x][y].strip(),
    #                                      distances[0][y].strip()))
    #
    #     stops[row[1][:-7].strip()] = stop_list

    # iterate over column titles
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

    for k, v in stops.items():
        print(k)
        for val in v:
            print(f'\t {val}')

    print(names_and_addresses)


def determine_distance(start, stop):
    # use stop name as key
    # search list of stops for corresponding value

    start_name = names_and_addresses.get(start)
    stop_name = names_and_addresses.get(stop)

    x = next(x for x in stops.get(stop_name) if x[1] == start_name)

    return float(x[0]), stop_name

    # starting_point_name = stops[start[1]]
    # distance = stop_list[position + 1][0]
    # stop_name = stop_list[position + 1][1]

    # print(f'{stop_name} has a distance of {distance} miles')
    #
    # return float(distance), stop_name


def determine_next_stop(start, list_of_stops):
    shortest_distance = 9999
    closest_stop = ''

    for x, stop in enumerate(list_of_stops):
        # print(f'stop "{stop}"', end=' ')
        distance, stop_name = determine_distance(start, stop)

        if distance < shortest_distance:
            shortest_distance = distance
            closest_stop = stop_name
            # print(f'current shortest_distance: {shortest_distance}')

    print(f'shortest distance distance: {shortest_distance} miles'
          f', next stop is: {closest_stop}\n')


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

    for package in hm:
        print(package)


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


def print_line_break():
    print('*' * 100)
