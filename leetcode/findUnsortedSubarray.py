class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortedList = sorted(nums)
        start, end = None, None
        
        for i in range(len(nums)):
            if sortedList[i] != nums[i]:
                if start == None: 
                    start = i
                else:
                    end = i
        if start == None and end == None:
            return 0
        elif end == None:
            return 2
        return end - start + 1
