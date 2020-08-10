class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_dict = dict()
        
        for i in nums:
            if i in nums_dict:
                nums_dict[i] += 1
            else:
                nums_dict[i] = 1
                
        sort_orders = sorted(nums_dict.items(), key=lambda x: x[1], reverse=True)
        ret_lst = []
        for i in range(k):
            ret_lst.append(sort_orders[i][0])
        return ret_lst
