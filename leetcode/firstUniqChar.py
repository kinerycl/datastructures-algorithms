class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = dict()
        for i in s:
            if i in letters:
                letters[i] +=1
            else:
                letters[i] =1
        for i in range(len(s)):
            if letters[s[i]] == 1:
                return i
        return -1
