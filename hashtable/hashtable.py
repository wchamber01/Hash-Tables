class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.head = None

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
        # Find the hash index
        index = self.hash_index(key)
        node = self.storage[index]
        new_node = HashTableEntry(key, value)
        # if node exists in storage
        if node:
            # then replace the value
            node = value
        # else create a new node
        else:
            new_node.next = self.head
            self.head = new_node

        return new_node

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        current = self.head
        # While current node exists
        while current:
            # If the current node's key is equal to the key being passed in
            if current.key == key:
                # Reset current node's key to None
                current.key = None
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
        current = self.head
        # While the current node exists
        while current:
            # If the current node's key is equal to the key being passed in
            if current.key == key:
                # Return current node's value
                return current.value
            else:
                # Advance current node to next node before looping
                current = current.next
        # Else return None
        return None

    def resize(self, new_capacity):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Implement this.
        """
        # double the capacity
        # self.capacity = new_capacity * 2
        new_storage = [None] * new_capacity
        for value in self.storage:
            if value:
                hashed_key = self.hash_index(value[0])
                new_storage[hashed_key] = value
        self.storage = new_storage


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
