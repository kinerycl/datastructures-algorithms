class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        unique_dict = dict()
        for i in arr:
            if i in unique_dict:
                unique_dict[i]+=1
            else:
                unique_dict[i]=1
                
        uni_arr = []
        for key, value in unique_dict.items():
            if value in uni_arr:
                return False
            else:
                uni_arr.append(value)
        return True
