class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total1 = 0
        total2 = 0
        for i in nums:
            temp = max(i+total1, total2)
            total1 = total2
            total2 = temp
        return total2
            
