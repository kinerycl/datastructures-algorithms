class Queue(object):
    def __init__(self):
        self.data = []
        self.count = 0

    def remove(self):
        if self.is_empty():
            return None
        self.count -= 1
        return self.data.pop(0)

    def add(self, item):
        self.count += 1
        self.data.append(item)

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.data[0]

    def is_empty(self):
        if self.count == 0:
            return True
        return False
