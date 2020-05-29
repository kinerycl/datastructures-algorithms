class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ret_array = []
        
        for i in A:
            if i%2 == 0:
                ret_array.insert(0, i)
            else:
                ret_array.append(i)
                
        return ret_array
