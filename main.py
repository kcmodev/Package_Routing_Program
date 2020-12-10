import data_parser as data
from delivery_algorithm import deliver_all_packages, display_time_window


def main():
    print()
    data.parse_distance_table()
    data.parse_package_file(package_file)
    print()

    while True:
        billboard()


def billboard():
    """
    Main screen for user interaction with the program. Runs until user initiated
    termination.
    :return:
    """
    data.print_line_break()
    print("""
            Please make a selection:
            1. Initiate package delivery algorithm.
            2. Search all packages (Run algorithm first to search package status after delivery.)
            3. See package status within a time window.
            4. Exit program.
            
    """)
    data.print_line_break()

    try:
        user_selection = int(input('Selection: '))

        if user_selection == 1:  # Run the delivery algorithm.
            deliver_all_packages()

        elif user_selection == 2:  # Search for package by package id.
            data.package_search(int(input('Enter the Package ID: ')))

        elif user_selection == 3:  # See package status within a window of time.
            data.print_line_break()
            print("""
            Please choose a time frame:
                1. Between 8:35am and 9:25am
                2. Between 9:35am and 10:25am
                3. Between 12:03pm and 1:12pm
            """)
            data.print_line_break()
            display_time_window(int(input('Selection: ')))

        elif user_selection == 4:  # Exit the program.
            print('Terminating program.')
            exit(1)

        # Raises a value error for an invalid choice and returns the user to the main
        # screen.
        else:
            raise ValueError

    except ValueError:
        print(f'Invalid choice. Try again.')
        billboard()


if __name__ == '__main__':
    package_file = 'data/Package File.csv'
    print('Running main...')
    main()
