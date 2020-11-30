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

    # iterates over csv file and adds each stop name value from each row[0]
    # as the key. Then adds the dict values as a list of destination and
    # distance pair for a time complexity of O(n^2)
    for x, row in enumerate(distances):
        if x > 0:  # skips first row
            for y, col in enumerate(row):  # iterates over the columns
                if 1 < y < len(row):
                    # assigns the miles column w/ the destination
                    # skipping the first stop which is the 'HUB'
                    if row[0] == 'Western Governors University' \
                            and distances[x][y] == '0.0':
                        continue
                    else:
                        stops[row[0]].append([distances[0][y],
                                             distances[x][y]])

    for k, v in stops.items():
        print(k)
        for val in v:
            print(f'\t {val}')


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
