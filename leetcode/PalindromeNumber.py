class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: 
            return False
        str_lst = list(str(x))
        str_lst.reverse()
        if int("".join(str_lst)) == x:
            return True
