class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        counts = dict()
        for n in nums:
            if n in counts:
                counts[n] +=1
            else:
                counts[n] = 1
        
        for key, val in counts.items():
            if val == 1:
                return key
