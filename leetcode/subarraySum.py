class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prev_sums ={0:1}
        curr_sum = 0
        count = 0
        
        for num in nums:
            curr_sum += num 
            
            if curr_sum - k in prev_sums:
                count += prev_sums[curr_sum-k]

            if curr_sum in prev_sums:
                prev_sums[curr_sum] +=1
            else:
                prev_sums[curr_sum] = 1
                
        return count
