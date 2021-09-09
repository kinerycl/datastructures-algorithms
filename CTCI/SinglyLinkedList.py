class Node(object):
    def __init__(self, data, node=None):
        self.data = data
        self.next = node

    def __str__(self):
        return str(self.data)


class SinglyLinked(object):
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

    def insert_head(self, node):
        node.next = self.head
        self.head = node

    def remove_head(self):
        if self.head is not None:
            if self.head.next is not None:
                self.head = self.head.next
            else:
                self.head = None

    def remove_tail(self):
        if self.head is not None and self.head.next is not None:
            prev = self.head
            curr = self.head.next
            while curr.next is not None:
                prev = curr
                curr = curr.next
            prev.next = None
        else:
            self.head = None

    def find_node(self, data):
        data = str(data)
        prev = None
        curr = self.head
        while curr is not None:
            if curr.data == data:
                return prev, curr
            prev = curr
            curr = curr.next
        else:
            return None, None

    def remove_node(self, data):
        prev, curr = self.find_node(data)
        if prev is None and curr is not None:
            self.head = curr.next
        elif curr is not None:
            prev.next = curr.next

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
