import data_parser as d_p


def main():
    print()
    d_p.parse_distance_table()
    # d_p.print_line_break()
    d_p.parse_package_file()
    print()

    while True:
        billboard()


def billboard():
    d_p.print_line_break()
    print("""
            Please make a selection:
            1. Search all Packages
            2. Search all Hubs
    """)
    d_p.print_line_break()

    user_selection = int(input('Selection: '))

    if user_selection == 1:
        d_p.package_search(int(input('Enter the Package ID: ')))
    elif user_selection == 2:
        d_p.hub_search(input('Enter the name of the hub: '))
    else:
        print('Invalid choice.')
        billboard()


if __name__ == '__main__':
    main()
