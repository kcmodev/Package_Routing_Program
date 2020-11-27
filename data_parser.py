import csv
from hashmap import HashMap
from collections import defaultdict

hm = HashMap()
stops = defaultdict(list)


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


    for row in reversed(distances):
        stop_name = row[0]
        for x, field in enumerate(row):
            if field > 1:
                stops[stop_name].append(

                )

        # temp = []
        # for x, line in enumerate(lines):
        #     temp.append(line)

        # for x, row in enumerate(temp):
        #     # if x > 0:
        #     stops[row[0]] = []
        #     for y, column in enumerate(row):
        #         fields = list(column.split(','))
        #         if y > 1:
        #             stops[row[0]].append(fields)

        # for k, v in stops.items():
        #     print(k, v)
        # iterate over locations in reverse and associate mileage with
        # each stop and it's destination options


# def add_waypoint(from_vertex, to_vertex, distance):
#     waypoint = (from_vertex, to_vertex, distance)
#     return waypoint


def parse_package_file():
    """
    Parses csv file `Package File` and fills a list with the data. Uses
    `package id` as the index for the list to make searching O(1)
    :return: None. Fills list with parsed data.
    """

    print('Package file loaded and parsed....')
    with open('data/Package File.csv') as distance_table:
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
                note = line[7]
                delivery_status = ''

                hm.__setitem__(package_id, address, deadline, city, zipcode,
                               weight, delivery_status)

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


def print_line_break():
    print('*' * 100)
