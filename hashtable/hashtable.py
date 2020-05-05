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
        index = self.hash_index(key)
        node = self.storage[index]
        # if key exists in storage
        if node:
            # then replace the value
            node = value
        # else create a new entry with HashTableEntry
        else:
            HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        self.storage[index] = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        if index:
            return self.storage[index]
        else:
            return None

    def resize(self, new_capacity):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Implement this.
        """
        # double the capacity
        self.capacity *= 2
        new_storage = [None] * self.capacity
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
    new_capacity = len(ht.storage)
    ht.resize(new_capacity)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
