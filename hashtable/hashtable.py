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
        index = self.hash_index(key)
        node = self.storage[index]
        HTE = HashTableEntry(key, value)

        if node is None:
            self.storage[index] = HTE
            return
            # Assign the next value of the index to the hash

        prev = node
        while node is not None:
            if node.key == key:
                node.value = value
                return

            prev = node
            node = node.next

        prev.next = HTE

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        current = self.head
        load_factor = None
        # While current node exists and starting at the head
        while current:
            # If the current node's key is equal to the key being passed in
            if current.key == key:
                # Reset current node's key to None
                current.key = None
                # Reduce key_count by 1
                self.key_count -= 1
                # Set a new load_factor with the reduced key_count
                load_factor = self.key_count / self.capacity
                # If load_factor is < 0.2
                if load_factor < 0.2:
                    # Halve the size of the hashtable
                    self.resize(self.capacity // 2)
                    # Set load_factor to new size
                    load_factor = self.key_count / self.capacity
            else:
                # Advance current node to next node before looping
                current = current.next
        # If no more nodes exist return none
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

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
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

        new_storage = [None] * new_capacity
        old_storage = self.storage
        self.storage = new_storage
        for node in old_storage:
            while node is not None:
                self.put(node.key, node.value)
                node = node.next

        # each_slot = 0
        # for node in self.storage:
        #     each_slot += 1

        # load_factor = self.key_count / each_slot


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    new_capacity = len(ht.storage) * 2
    ht.resize(new_capacity)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
