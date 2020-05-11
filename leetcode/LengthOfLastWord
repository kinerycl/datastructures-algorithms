class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """        
        lastLen = 0
        
        for i in range(len(s)-1, -1, -1):
            if s[i] == " " and lastLen > 0:
                return lastLen
            if s[i].isalpha():
                lastLen+=1
            
        return lastLen
