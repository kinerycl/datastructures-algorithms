class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        scode_dict = dict()
        tcode_dict = dict()
        
        for i in range(len(s)):
            if s[i] in scode_dict:
                if scode_dict[s[i]] != t[i]:
                    return False
            else:
                scode_dict[s[i]] = t[i]
             
            if t[i] in tcode_dict:
                if tcode_dict[t[i]] != s[i]:
                    return False
            else:
                tcode_dict[t[i]] = s[i]
                
        return True
