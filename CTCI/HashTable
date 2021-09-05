class HashTable(object):
    def __init__(self):
        self.MAX = 100
        self.data = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        k_hash = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.data[k_hash]):
            if len(element) == 2 and element[0] == key:
                self.data[k_hash][idx] = (key, value)
                found = True
                break
        if not found:
            self.data[k_hash].append((key, value))

    def __getitem__(self, key):
        k_hash = self.get_hash(key)
        for element in self.data[k_hash]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        k_hash = self.get_hash(key)
        for idx, element in enumerate(self.data[k_hash]):
            if element[0] == key:
                del self.data[k_hash][idx]
