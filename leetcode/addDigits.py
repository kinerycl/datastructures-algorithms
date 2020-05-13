class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        str_num = str(num)
        sum_int = 0
        
        for num in str_num:
            sum_int += int(num)
        
        if sum_int < 10:
            return sum_int
        
        return self.addDigits(sum_int)
