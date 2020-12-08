import data_parser as data


class HashMap:

    def __init__(self):
        self.hashmap = []

    # method serves at the insertion function
    # appends an item onto the hashmap - O(1)
    # automatically appends new packages to the end of the hashmap
    def __setitem__(self, package_id, address, deadline, city, zipcode,
                    weight, special_note=None, delivery_status='At the hub',
                    new_package=False):
        """
        Takes input add a record to the HashMap class list `hashmap`. Uses
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
        self.hashmap.append([package_id, [
            address,
            deadline,
            city,
            zipcode,
            weight,
            special_note,
            delivery_status
        ]])

    # look-up function
    # returns an item from the hashmap - O(n)
    def get_package_id(self, address):
        for x, package in enumerate(self.hashmap):
            if self.hashmap[x][1][0] == data.get_address_from_name(address):
                return self.hashmap[x][0]

    def set_delivery_status(self, package_id, status):
        """
        Takes package id as input to set delivery status for a package in the
        hashmap
        :param package_id:
        :param status:
        :return:
        """

        for x, package in enumerate(self.hashmap):
            if package[0] == package_id:
                self.hashmap[x][1][6] = status
                break

    def set_special_note(self, package_id, note):
        for x, package in enumerate(self.hashmap):
            if package[0] == package_id:
                self.hashmap[x][1][5] = note
                break

    def set_address(self, package_id, address):
        for x, package in enumerate(self.hashmap):
            if package[0] == package_id:
                self.hashmap[x][1][0] = address
                break

    def resize_hashmap(self, num_to_add):
        """
        Resizes the hashmap by appending blank entries to the end of the list. The
        number of additional spaces would be determined by the user and would be
        initialized with None. O(n).
        :return:
        """

        for num in num_to_add:
            self.hashmap.append(None)

    # implements an iterator function for the hashmap class O(n)
    def __iter__(self):
        return iter(self.hashmap)

    # implements a len function for the hashmap to enable resizing based on
    # the length of the current hashmap
    def __len__(self):
        return len(self.hashmap)

    def __getitem__(self, item):
        return self.hashmap[item]
