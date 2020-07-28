class Solution(object):
    def __init__(self):
        self.total = 0
        self.array = []
        self.memory = dict()
        self.target = 0

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.array = nums
        self.target = S
        
        return self.getCount(0, 0)
        
    def getCount(self, index, count):
        if index == len(self.array):
            if count == self.target:
                return 1
            else:
                return 0
            
        if (count, index) in self.memory:
            return self.memory[(count, index)]
        
        total = self.getCount(index+1, count+self.array[index]) + self.getCount(index+1, count-self.array[index])
        
        self.memory[(count, index)] = total
        
        return total
