class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            j = i + 1
            for k in range(j, len(nums)):
                if nums[i] + nums[k] == target:
                    return [i, k]
            
        
