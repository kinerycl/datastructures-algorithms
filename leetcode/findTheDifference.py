class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letters = dict()
        for letter in s:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        
        for let in t: 
            if let in letters:
                if letters[let] == 0:
                    return let
                else:
                    letters[let] -= 1
            else:
                return let
