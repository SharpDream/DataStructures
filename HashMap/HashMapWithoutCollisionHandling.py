# implementing Hash Table without handeling collision


class HashTable:

    def __init__(self):
        self.max = 100
        self.arr = [None] * self.max

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.max

    def __setitem__(self, key, val):
        index = self.get_hash(key)
        self.arr[index] = val

    def __getitem__(self, key):
        index = self.get_hash(key)
        return self.arr[index]

    def __delitem__(self, key):
        index = self.get_hash(key)
        self.arr[index] = None
