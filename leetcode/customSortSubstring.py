class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        order_str = ""
        for letter in S:
            if letter in T:
                order_str += letter * T.count(letter)
                T = T.replace(letter, "")
        return order_str + T
