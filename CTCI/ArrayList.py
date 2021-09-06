class ArrayList(object):
    def __init__(self):
        self._size = 5
        self._data = [0 for i in range(self._size)]
        self._count = 0

    def __double(self):
        for i in range(self._size):
            self._data.append(None)
        self._size *= 2

    def is_full(self):
        if self._size == self._count:
            return True
        return False

    def is_empty(self):
        if self._count == 0:
            return True
        return False

    def insert(self, val):
        if self.is_full():
            self.__double()
        self._data[self._count] = val
        self._count += 1

    def remove(self):
        if self.is_empty():
            return None
        self._count -= 1
        self._data[self._count] = None

    def current_data(self):
        print(self._data)
