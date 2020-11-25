import csv

packages = []
stops = []


def parse_distance_table():
    """
    Parses csv file `Distance Table` and fills a list with the data. Uses
    `package id` as the index for the list to make searching O(1)
    :return: None. Fills list with parsed data.
    """
    global stops

    print('Distance table loaded and parsed.')
    with open('data/Distance Table.csv') as distance_table:
        lines = csv.reader(distance_table)

        # enumerate and fill distance data O(n)
        for x, line in enumerate(lines):
            stops.append([line[0], line[1:]])

    for stop in stops:
        print(stop)


def parse_package_file():
    """
    Parses csv file `Package File` and fills a list with the data. Uses
    `package id` as the index for the list to make searching O(1)
    :return: None. Fills list with parsed data.
    """
    global packages

    print('Package file loaded and parsed.')
    with open('data/Package File.csv') as distance_table:
        lines = csv.reader(distance_table)

        # enumerate and fill package hash table O(n)
        for x, line in enumerate(lines):
            if x != 0:
                packages.append([int(line[0]), line[1:]])

    for package in packages:
        print(package)


def package_search(package_id: int) -> object:
    """
    Takes in package ID and returns all package data.
    :param package_id:
    :return: Package information
    """
    print_line_break()
    print()
    print(f'Package ID #{package_id} information:\n')
    print(packages[package_id - 1])
    print()


def hub_search(name: str) -> object:
    """
    Take in name of a hub and returns all hub data
    :param name:
    :return:  Hub data
    """
    print_line_break()
    print()
    print(f'HUB: {stops.index(name)}')
    print()


def print_line_break():
    print('*' * 100)
