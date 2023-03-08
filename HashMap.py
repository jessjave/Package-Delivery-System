# C950 - Webinar-1 - Let's Go Hashing
# C950 - Webinar-2 - Getting Greedy, who moved my data?
# Ref: zyBooks: Figure 7.8.2: Hash table using chaining.

class HashMap:
    # Constructor with capacity parameter.
    # Assigns all buckets with an empty list.
    # O(n) time and space
    def __init__(self, table_capacity=39):
        # initialize the hash table with empty bucket list entries.
        self.list = []
        for i in range(table_capacity):
            self.list.append([])

    # Inserts a new key value pair into the hash table.
    # O(n) time O(1) space
    def insert(self, key, item):
        # get the bucket list where this pair will go.
        bucket = hash(key) % len(self.list)
        full_list = self.list[bucket]

        # update the value if the key is already in the bucket
        for pair in full_list:
            if pair[0] == key:
                pair[1] = item
                return True

        # if not, insert the key value pair to the end of the bucket list.
        key_value = [key, item]
        full_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the key value pair if found, or None if not found.
    # O(n) time O(1) space
    def lookup(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.list)
        full_list = self.list[bucket]

        # search for the key in the bucket list
        for pair in full_list:
            # print (key_value)
            if pair[0] == key:
                return pair[1]  # value
        return None

    # Removes an item with matching key from the hash table.
    # O(n) time O(1) space
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.list)
        full_list = self.list[bucket]

        # remove the item from the bucket list if it is present.
        for pair in full_list:
            if pair[0] == key:
                full_list.remove(pair[0], pair[1])
