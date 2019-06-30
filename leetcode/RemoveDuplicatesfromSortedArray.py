class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        length = len(nums)-1
        while i < length: #stop one before end
            if nums[i] == nums[i+1]:
                nums.pop(i)
                length -= 1
            else:
                i += 1

