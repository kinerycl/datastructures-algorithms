class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        letters = dict()
        for i in s:
            if i in letters:
                letters[i] +=1
            else:
                letters[i] = 1
        
        for i in t:
            if i not in letters:
                return False
            else:
                letters[i] -=1
                if letters[i] == -1:
                    return False
                
        return True
