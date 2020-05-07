class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        # self.head = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.key_count = 0

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function
        Implement this, and/or DJB2.
        """
        hash_ = 14695981039346656037
        for k in key:
            hash_ = hash_ ^ ord(k)
            hash_ = hash_ * 1099511628211
            hash_ &= 0xffffffffffffffff
        return hash_

    def djb2(self, key):
        """
        DJB2 32-bit hash function
        Implement this, and/or FNV-1.
        """
        hash_ = 5381
        for k in key:
            hash_ = (hash_ * 33) + ord(k)
            hash_ &= 0xffffffff
        return hash_

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def calc_load_factor(self):
        load_factor = self.key_count / self.capacity
        if load_factor > 0.7:
            self.resize(self.capacity*2)
        elif load_factor < 0.2 and self.capacity > 8:
            self.resize(load_factor // 2)

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # # Find the hash index
        # # if node exists in storage
        # # then replace the value
        # # else create a new node
        # # Create
        # # Set key_count
        # # Set load_factor
        # return new_node

        # Define the hash index/key
        index = self.hash_index(key)
        # Define the storage index
        node = self.storage[index]
        HTE = HashTableEntry(key, value)
        prev = None

        # print('load_factor ln 76:', load_factor)

        if node is None:
            self.storage[index] = HTE
            self.key_count += 1
            self.calc_load_factor()
            return

        if node.key == key:
            node.value = value
            return

        while node.key != key:
            if node.next is None:
                node.next = HTE
                self.key_count += 1
                self.load_factor()
                return
            node = node.next

            if node.key == key:
                node.value = value
                return

        # if load_factor > 0.7:
        #     self.resize(self.capacity*2)
        # return
        #     # Assign the next value of the index to the hash

        # # while node is not None:
        # if node.key == key:
        #     node.value = value
        #     return
        # while node.key != key:
        #     if node.next is None:
        #         node.next = HTE
        #         self.key_count += 1
        #         if load_factor > 0.7:
        #             self.resize(self.capacity*2)
        #         return
        #     node = node.next
        #     if node.key == key:
        #         node.value = value
        #         return

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # current = self.head
        # load_factor = None
        # While current node exists and starting at the head
        # while current:
        #     # If the current node's key is equal to the key being passed in
        #     if current.key == key:
        #         # Reset current node's key to None
        #         current.key = None
        #         # Reduce key_count by 1
        #         self.key_count -= 1
        #         # Set a new load_factor with the reduced key_count
        #         load_factor = self.key_count / self.capacity
        #         # If load_factor is < 0.2
        #         if load_factor < 0.2:
        #             # Halve the size of the hashtable
        #             self.resize(self.capacity // 2)
        #             # Set load_factor to new size
        #             load_factor = self.key_count / self.capacity
        #     else:
        #         # Advance current node to next node before looping
        #         current = current.next
        # # If no more nodes exist return none
        # return None

        # index = self.hash_index(key)
        # node = self.storage[index]
        # prev = None

        # while node is not None and node.key != key:
        #     prev = node
        #     node = node.next

        # if node is None:
        #     return None
        # elif node.key == key and node.next is not None:
        #     prev.next = node.next
        #     node.key = None
        # elif node.next is None and node.key == key:
        #     self.storage[index] = None

        index = self.hash_index(key)
        node = self.storage[index]
        prev = None

        if node is None or self.key_count == 0:
            return None

        if node.next is None:
            if node.key == key:
                del_value = node.value
                self.storage[index] = None
                self.key_count -= 1
                self.calc_load_factor()
                return del_value
            else:
                return None

        while node:
            if node.key == key:
                del_value = node.value
                self.key_count -= 1
                node.key = None
                prev.next = node.next
                self.calc_load_factor()
                return del_value
            prev = node
            node = node.next
        return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # current = self.head
        # # While the current node exists
        # while current:
        #     # If the current node's key is equal to the key being passed in
        #     if current.key == key:
        #         # Return current node's value
        #         return current.value
        #     else:
        #         # Advance current node to next node before looping
        #         current = current.next
        # # Else return None
        # return None
        index = self.hash_index(key)
        node = self.storage[index]

        if node is None:
            return None
        while node.key != key:
            if node.next is None:
                return None
            node = node.next
        return node.value

    def resize(self, new_capacity):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Implement this.
        """
        # double the capacity
        # self.capacity = new_capacity * 2
        # new_storage = [None] * new_capacity
        # for value in self.storage:
        #     if value:
        #         hashed_key = self.hash_index(value[0])
        #         new_storage[hashed_key] = value
        # self.storage = new_storage

        # old_storage = self.storage
        # print('new_capacity:', new_capacity)
        self.capacity = new_capacity
        self.capacity = max((self.capacity), 8)
        new_storage = [None] * self.capacity
        for node in self.storage:
            if node is not None:
                hashed_key = self.hash_index(node.key)
                new_storage[hashed_key] = node
            self.storage = new_storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    # print('key 1:', ht.key_count, '\n')
    ht.put("line_2", "Filled beyond capacity")
    # print('key 2:', ht.key_count, '\n')
    ht.put("line_3", "Linked list saves the day!")
    # print('key 3:', ht.key_count, '\n')

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    # print('old_capacity:', old_capacity)
    new_capacity = len(ht.storage) * 2
    # print('new_capacity:', new_capacity)
    ht.resize(new_capacity)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
