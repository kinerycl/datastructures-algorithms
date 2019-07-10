class Solution(object):
  #kadane's algorithm
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCurr = maxGlob = nums[0]
        for i in range(1, len(nums)):
            maxCurr = max(nums[i], maxCurr + nums[i])
            if maxCurr > maxGlob:
                maxGlob = maxCurr
        return maxGlob

