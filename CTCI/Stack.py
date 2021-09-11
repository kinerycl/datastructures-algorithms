class Stack(object):
    def __init__(self):
        self.data = []
        self.count = 0

    def pop(self):
        if self.is_empty():
            return None
        self.count -= 1
        return self.data.pop(0)

    def push(self, item):
        self.count += 1
        self.data.insert(0, item)

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.data[0]

    def is_empty(self):
        if self.count == 0:
            return True
        return False
