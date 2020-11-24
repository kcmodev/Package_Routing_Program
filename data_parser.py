import csv

class Package:

    def __init__(self, package_id, address, city, state, zip_code,
                               delivery_deadline, mass, special_notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.mass = mass
        self.special_notes = special_notes

# class TruckStop:
#
#     def __init__(self):


def parse_distance_table():
    print('Distance table loaded and parsed.')
    with open('data/Distance Table.csv') as distance_table:
        lines = csv.reader(distance_table)

        for x, line in enumerate(lines):
            # print(f'Line #{x}: {line}')
            pass


def parse_package_file():
    packages = []

    print('Package file loaded and parsed.')
    with open('data/Package File.csv') as distance_table:
        lines = csv.reader(distance_table)

        for x, line in enumerate(lines):
            packages.append([line[0], line[1], line[2], line[3], line[4],
                             line[5], line[6]])

    for package in packages:
        print(package)


def package_search(package_id: int):
    print(f'Package ID #{package_id} information:\n')


def print_line_break():
    print('*' * 200)
