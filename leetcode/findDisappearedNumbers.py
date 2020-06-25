class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            index = abs(nums[i]) -1
            if nums[index] > 0:
                nums[index]  *= -1
            
        absent = []
        for i in range(0, len(nums)):
            if nums[i] > 0:
                absent.append(i+1)
        return absent
