import csv


def parse_distance_table():
    print()
    print('*' * 100)
    with open('data/Distance Table.csv') as distance_table:
        lines = csv.reader(distance_table, delimiter=',')

        for x, line in enumerate(lines):
            print(f'Line #{x}: {line}')

    print('*' * 150)


def parse_package_file():
    print()
    print('*' * 150)

    with open('data/Package File.csv') as distance_table:
        lines = csv.reader(distance_table, delimiter=',')

        for x, line in enumerate(lines):
            print(f'Line #{x}: {line}')

    print('*' * 100)
