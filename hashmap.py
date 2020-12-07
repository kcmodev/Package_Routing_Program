import data_parser as data


class HashMap:

    def __init__(self):
        self.hashmap = []

    # method inserts an item into the hashmap - O(1)
    # automatically appends new packages to the end of the hashmap with a
    # generated package id making this data structure self-adjusting
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

        # not a new package, used for initializing the hashmap
        if new_package is False:
            self.hashmap.append([package_id, [
                address,
                deadline,
                city,
                zipcode,
                weight,
                special_note,
                delivery_status
            ]])
        # user entering a new package into the list
        # add functionality later to enable entering of special notes
        else:
            # uses length of the list to determine the next available number
            # for the package ID
            # could add function later to remove unused package numbers and
            # append packages to the spaces in the list
            self.hashmap.append([(len(self.hashmap) + 1), [
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
        # self.hashmap[int(package_id) - 1][1][6] = status
        for x, package in enumerate(self.hashmap):
            if package[0] == package_id:
                self.hashmap[x][1][6] = status
                break

    # implements an iterator function for the hashmap class O(n)
    def __iter__(self):
        return iter(self.hashmap)

    # implements a len function for the hashmap to enable resizing based on
    # the length of the current hashmap
    def __len__(self):
        return len(self.hashmap)

    def __getitem__(self, item):
        return self.hashmap[item]
