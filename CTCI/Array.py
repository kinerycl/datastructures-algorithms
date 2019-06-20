class Vector:
    def __init__(self):
        self.size = 0
        self.capacity = 16
        self.vector = []

    def size(self):
        return self.size

    def capacity(self):
        return self.capacity

    def is_empty(self):
        return self.size == 0

    def at(self, index):
        return self.vector[index]

    def push(self, item):
        self.vector.append(item)
        self.size += 1
        if self.size is self.capacity:
            self.__resize(self.capacity * 2)

    def insert(self, index, item):
        self.vector[index] = item
        self.size += 1
        if self.size is self.capacity:
            self.__resize(self.capacity * 2)

    def prepend(self, item):
        self.vector.insert(0, item)
        self.size += 1
        if self.size is self.capacity:
            self.__resize(self.capacity * 2)

    def pop(self):
        self.size -= 1
        if self.size == self.capacity//4:
            self.__resize(self.capacity//2)
        return self.vector.pop()

    def delete(self, index):
        if index > self.size -1:
            return
        self.size -= 1
        if self.size == self.capacity // 4:
            self.__resize(self.capacity // 2)
        for i in range(index, self.size):
            self.vector[i] = self.vector[i +1]
        self.vector.pop()

    def remove(self, item):
        if self.size == self.capacity // 4:
            self.__resize(self.capacity // 2)
        index = 0
        while self.size is not 0:
            if index > self.size -1:
                break
            elif self.vector[index] is item:
                self.delete(index)
            else:
                index += 1

    def find(self, item):
        for i in range(self.size):
            if self.vector[i] is item:
                return i
        return -1

    def __resize(self, new_capacity):
        self.capacity = new_capacity

vect = Vector()
for i in range(5):
    vect.push(3)
vect.push(1)
print(vect.vector)
print(vect.size)
print(vect.capacity)

print(vect.find(1))
print(vect.vector)
print(vect.remove(3))
print(vect.vector)

