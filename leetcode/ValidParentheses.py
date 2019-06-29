class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return check(s)
    
def check(s):
    if s == "":
        return True
    bracs = ["()" , "[]", "{}"]
    for brac in bracs:
        if brac in s:
            b_in = s.find(brac)
            b_lst = list(s)
            b_lst.pop(b_in+1)
            b_lst.pop(b_in)
            return check("".join(b_lst))
    return False
    
   
