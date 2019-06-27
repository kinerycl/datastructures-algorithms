class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        
        max_pre = min(strs, key=len)
        if max_pre == "":
            return ""
        strs.remove(max_pre)
        index = len(max_pre) - 1
        count_beg = False
        ans = False
        
        while ans == False:
            brk = False
            for word in strs:
                if word[:index] != max_pre[:index]: #False
                    if index == 0:
                        return ""
                    elif count_beg is True:
                        return max_pre[:index-1] #passed index
                    else:
                        index = index /2
                        brk = True
                        break
            if brk is True:
                continue
            count_beg = True
            if index == len(max_pre): #all are max
                return max_pre
            index += 1
