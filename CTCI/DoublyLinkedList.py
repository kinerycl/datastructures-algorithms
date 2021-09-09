class Node(object):
    def __init__(self, data, after=None, prev=None):
        self.data = data
        self.next = after
        self.prev = prev

    def __str__(self):
        return str(self.data)


class DoublyLinked(object):
    def __init__(self, node=None):
        self.head = node

    def insert_tail(self, node):
        curr = self.head
        if curr is None:
            self.head = node
        else:
            while curr.next is not None:
                curr = curr.next

            curr.next = node
            node.prev = curr

    def insert_head(self, node):
        if self.head is not None:
            node.prev = None
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            node.prev = None
            self.head = node

    def remove_head(self):
        if self.head is not None:
            if self.head.next is not None:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None

    def remove_tail(self):
        if self.head is not None and self.head.next is not None:
            curr = self.head
            while True:
                if curr.next is None:
                    curr.prev.next = None
                    break
                curr = curr.next
        else:
            self.head = None

    def find_node(self, data):
        data = str(data)
        curr = self.head
        while curr is not None:
            if curr.data == data:
                return curr.prev, curr
            curr = curr.next
        else:
            return None, None

    def remove_node(self, data):
        prev, curr = self.find_node(data)
        if prev is None and curr is not None:
            if curr.next is None:
                self.head = None
            else:
                self.head = curr.next
                self.head.prev = None
        elif curr is not None:
            prev.next = curr.next
            curr.next.prev = prev

    def __str__(self):
        ret = ""
        node = self.head
        if node is None:
            return "Empty List"
        while node is not None:
            ret += str(node.data)
            ret += " "
            node = node.next
        return ret
