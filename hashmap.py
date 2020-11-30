# Develop a hash table, without using any additional libraries or classes,
# that has an insertion function that takes the following components as
# input and inserts the components into the hash table:
# • package ID number
# • delivery address
# • delivery deadline
# • delivery city
# • delivery zip code
# • package weight
# • delivery status (e.g., delivered, en route)

class HashMap:

    def __init__(self):
        self.hashmap = []

    # method inserts an item into the hashmap - O(1)
    # automatically appends new packages to the end of the hashmap with a
    # generated package id making this data structure self-adjusting
    def __setitem__(self, package_id, address, deadline, city, zipcode,
                    weight, special_note=None, delivery_status='Not Delivered',
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
        else:
            # uses length of the list to determine the next available number
            # for the package ID
            self.hashmap.append([len(self.hashmap), [
                address,
                deadline,
                city,
                zipcode,
                weight,
                special_note,
                delivery_status
            ]])

    # look-up function
    # returns an item from the hashmap - O(1)
    def __getitem__(self, item):
        return self.hashmap[item]

    def __iter__(self):
        return iter(self.hashmap)

    def __len__(self):
        return len(self.hashmap)
