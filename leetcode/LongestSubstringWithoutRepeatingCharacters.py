class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        highest = 0
        cur_str = ""
        count = 0
        i = 0
        while i < (len(s)):
            if s[i] not in cur_str:
                cur_str += s[i]
                count += 1
            else:
                cur_str = cur_str[cur_str.find(s[i]) + 1 :]
                cur_str += s[i]
                count = len(cur_str)
                
            if count > highest:
                highest = count
            i += 1
            
        return highest

