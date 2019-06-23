class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret_lst = list(str(x)) # string
        ret_lst.reverse()
        ret_str = "".join(ret_lst)
        if x < 0:
            if -2**31 < int(ret_str[:-1]) * -1 < 2**31 -1:
                return int(ret_str[:-1]) * -1
            return 0
        if -2**31 < int(ret_str) < 2**31 -1:
            return int(ret_str)
        return 0

