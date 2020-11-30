import data_parser as d_p


def main():
    print()
    d_p.parse_distance_table()
    d_p.parse_package_file(package_file)
    print()

    while True:
        billboard()


def billboard():
    d_p.print_line_break()
    print("""
            Please make a selection:
            1. Search all Packages
    """)
    d_p.print_line_break()

    try:
        user_selection = int(input('Selection: '))

        if user_selection == 1:
            d_p.package_search(int(input('Enter the Package ID: ')))
        else:
            raise ValueError

    except ValueError:
        print(f'Invalid choice. Try again.')
        billboard()


def search_for_package():
    pass


if __name__ == '__main__':
    package_file = 'data/TestPackageFile.csv'
    print('Running main...')
    main()
