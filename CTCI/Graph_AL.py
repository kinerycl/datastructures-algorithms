class Node(object):
    def __init__(self, val):
        self.vertex = val
        self.next = None


class Graph(object):
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d):
        node = Node(d)              # create new node
        node.next = self.graph[s]   # node points to s adj list
        self.graph[s] = node        # replace adj list with new 

        node = Node(s)              # create new node
        node.next = self.graph[d]   # node points to d adj list
        self.graph[d] = node        # replace adj list with new

    # Print the graph
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")
