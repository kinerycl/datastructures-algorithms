class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum = 0
        total_sum = sum(nums)
        for i in range(len(nums)):
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            else:
                left_sum += nums[i]
        return -1
