class MinHeap(object):
    def __init__(self):
        self.heap = []
        self.length = 0

    def parent(self, i):
        return int((i-1)/2)

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def has_parent(self, i):
        return self.parent(i) >= 0

    def has_left_child(self, i):
        return self.left_child(i) < self.length

    def has_right_child(self, i):
        return self.right_child(i) < self.length

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def bubble_up(self, i):
        while (self.has_parent(i)) and (self.heap[i] < self.heap[self.parent(i)]):
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def bubble_down(self, i):
        while self.has_left_child(i) or self.has_right_child(i):
            has_right = self.has_right_child(i)
            has_left = self.has_left_child(i)

            left = self.left_child(i)
            right = self.right_child(i)

            if (has_right and has_left is False) or (has_right and has_left and self.heap[left] > self.heap[right]):
                if self.heap[i] >= self.heap[right]:
                    self.swap(i, right)
                    i = right
                else:
                    break
            elif (has_left and has_right is False) or (has_right and has_left and self.heap[left] < self.heap[right]):
                if self.heap[i] >= self.heap[left]:
                    self.swap(i, left)
                    i = left
                else:
                    break

    def insert(self, val):
        self.length += 1
        self.heap.append(val)
        self.bubble_up(self.length-1)

    def extract_min(self):
        self.swap(0, self.length-1)
        self.heap.pop(self.length-1)
        self.length -= 1
        self.bubble_down(0)

    def get_min(self):
        return self.heap[0]

    def print_heap(self):
        print(self.heap)
