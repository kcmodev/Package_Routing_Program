import data_parser as data


class HashTable:

    def __init__(self):
        self.hashtable = []
        self.all_packages_loaded = False

    # Method serves as an insertion function appending an item onto the hashtable. 1
    # package per bucket. O(n).
    # Automatically appends new packages to the end of the hashtable. O(1).
    def __setitem__(self, package_id, address, deadline, city, zipcode,
                    weight, special_note=None, delivery_status='At the hub'):
        """
        Serves as an insertion function. Initial fill O(n).
        Appending items after a resize  O(1).

        Takes input add a record to the Hashtable class list `hashtable`. Uses
        package ID as the key and the remainder of the line data as a list
        of values associated with the key.
        :param package_id:
        :param address:
        :param deadline:
        :param city:
        :param zipcode:
        :param weight:
        :param delivery_status:
        :return:
        """

        self.hashtable.append([package_id, [
            address,
            deadline,
            city,
            zipcode,
            weight,
            special_note,
            delivery_status
        ]])

    def get_package_id(self, address):
        """
        Serves as the lookup function. Iterates through the hashtable and returns a
        package based on address. O(n).
        :param address:
        :return:
        """

        for x, package in enumerate(self.hashtable):
            if self.hashtable[x][1][0] == data.get_address_from_name(address):
                return self.hashtable[x][0]

    def set_delivery_status(self, package_id, status):
        """
        Takes package id as input to set delivery status for a package in the
        hashtable.
        :param package_id:
        :param status:
        :return:
        """

        for x, package in enumerate(self.hashtable):
            if package[0] == package_id:
                self.hashtable[x][1][6] = status
                break

    def set_special_note(self, package_id, note):
        """
        Takes package id as input to change a package's 'special note' section.
        :param package_id:
        :param note:
        :return:
        """

        for x, package in enumerate(self.hashtable):
            if package[0] == package_id:
                self.hashtable[x][1][5] = note
                break

    def set_address(self, package_id, address):
        """
        Sets a package's address based on package id.
        :param package_id:
        :param address:
        :return:
        """

        for x, package in enumerate(self.hashtable):
            if package[0] == package_id:
                self.hashtable[x][1][0] = address
                break

    def resize_hashtable(self, num_to_add):
        """
        Resizes the hashtable by appending blank entries to the end of the list. The
        number of additional spaces would be determined by the user and would be
        initialized with None. O(n).
        :return:
        """

        for num in num_to_add:
            self.hashtable.append(None)

    def __len__(self):
        """
        Function gives hashtable the len function to enable determining the amount of
        total
        packages to be delivered. O(1).
        :return:
        """
        return len(self.hashtable)

    def __getitem__(self, item):
        """
        Function makes hashtable subscriptable which allows selecting individual packages
        to be loaded onto a truck. O(1)
        :param item:
        :return:
        """
        return self.hashtable[item]
