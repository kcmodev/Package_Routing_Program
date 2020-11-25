import csv

packages = []


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
    """
    Parses csv file `Package File` and fills a list with the data. Uses
    `package id` as the index for the list to make searching O(1)
    :return: None. Fills list with imported data.
    """
    global packages

    print('Package file loaded and parsed.')
    with open('data/Package File.csv') as distance_table:
        lines = csv.reader(distance_table)

        for x, line in enumerate(lines):
            if x != 0:
                package_id = int(line[0])
                address = line[1]
                city = line[2]
                state = line[3]
                zip_code = line[4]
                deadline = line[5]
                mass = line[6]

                if line[7] is not None:
                    note = line[7]
                else:
                    note = None

                # package = Package(package_id, address, city, state,
                #                   zip_code, deadline, mass, note)
                #
                # packages.append([getattr(package, 'package_id'), [
                #     getattr(package, 'address'),
                #     getattr(package, 'city'),
                #     getattr(package, 'state'),
                #     getattr(package, 'zip_code'),
                #     getattr(package, 'delivery_deadline'),
                #     getattr(package, 'mass'),
                #     getattr(package, 'special_notes')
                # ]])
                packages.append([package_id, [address, city, state, zip_code,
                                              deadline, mass, note]])

    # for package in packages:
    #     print(package)


def package_search(package_id: int) -> object:
    print_line_break()
    print()
    print(f'Package ID #{package_id} information:\n')
    print(packages[package_id - 1])
    print()

def print_line_break():
    print('*' * 100)
