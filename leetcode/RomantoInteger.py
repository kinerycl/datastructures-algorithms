class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret_int = 0
        nums_dict = {"I":1, "IV":4, "V":5, "IX":9, "X":10, "XL":40, "L":50, "XC":90, "C":100, "CD":400, "D":500, "CM":900, "M":1000}

        i = 0 
        while i < len(s):
            if i == len(s)-1:#end
                ret_int += nums_dict[s[i]]
            elif s[i:i+2] in nums_dict: #check two
                ret_int += nums_dict[s[i:i+2]]
                i += 2
                continue
            else:
                ret_int += nums_dict[s[i]]
            i += 1
        return ret_int
