import data_parser as data
from delivery_algorithm import deliver_all_packages


def main():
    print()
    data.parse_distance_table()
    data.parse_package_file(package_file)
    print()

    while True:
        billboard()


def billboard():
    data.print_line_break()
    print("""
            Please make a selection:
            1. Initiate package delivery algorithm
            2. Search all packages
            3. Exit
            
    """)
    data.print_line_break()

    try:
        user_selection = int(input('Selection: '))

        if user_selection == 1:
            deliver_all_packages()

        elif user_selection == 2:
            data.package_search(int(input('Enter the Package ID: ')))

        elif user_selection == 3:
            print('Terminating program.')
            exit(1)

        else:
            raise ValueError

    except ValueError:
        print(f'Invalid choice. Try again.')
        billboard()


if __name__ == '__main__':
    package_file = 'data/TestPackageFile.csv'
    # package_file = 'data/Package File.csv'
    print('Running main...')
    main()
