class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mins = []
        self.minlen = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if self.minlen > 0:
            min_val = self.mins[-1]
            if min_val < x:
                self.mins.append(min_val)
            else:
                self.mins.append(x)
        else:
            self.mins.append(x)
        self.minlen+=1

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop(-1)
        self.mins.pop(-1)
        self.minlen-=1

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
