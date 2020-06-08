class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = dict()
        length = len(nums)//2
        for num in nums:
            #length +=1
            if num in counts: 
                counts[num] += 1
                if counts[num] > length:
                    return num
            else:
                counts[num] = 1
        
        return num

