import data_parser as d_p


def main():
    d_p.parse_distance_table()
    # d_p.print_line_break()
    d_p.parse_package_file()

    while True:
        billboard()


def billboard():
    print("""
            Please make a selection:
            1. Search by package ID
    """)

    user_selection = int(input('Selection: '))

    if user_selection == 1:
        package = int(input('Enter the Package ID: '))
        d_p.package_search(package)
    else:
        print('Invalid choice.')
        billboard()


if __name__ == '__main__':
    main()
