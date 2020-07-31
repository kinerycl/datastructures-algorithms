class Solution(object):
    def __init__(self):
        self.state = dict()
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total%2 == 1:
            return False
        
        return self.findPartition(nums, 0, 0, total)
    
    def findPartition(self, nums, index, working_sum, total):
        if (index, working_sum) in self.state:
            return self.state[(index, working_sum)]
        if working_sum *2 == total:
            return True
        if working_sum > total/2 or index >= len(nums):
            return False
        foundPartition = self.findPartition(nums, index+1, working_sum, total) or self.findPartition(nums, index+1, working_sum +nums[index], total)
        
        self.state[(index, working_sum)] = foundPartition
        return foundPartition
