class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            return nums.index(target)
        except:
            for num in nums:
                if target < num:
                    return nums.index(num) #replace
            return len(nums)   #end
