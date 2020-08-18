class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == '':
            return True
        if t == '':
            return False
        slst = []
        for let in s:
            slst.append(let)
            
        for let in t:
            if let == slst[0]:
                slst.pop(0)
            if len(slst) == 0:
                return True
        return False
