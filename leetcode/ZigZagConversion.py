class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
            return s
        inc = True
        i = 0 #index
        cnt = 1
        ret_str = ""
        str_dict = dict()
        for j in range(1, numRows+1): #initalize
            str_dict[j] = ""

        while i < len(s):
            str_dict[cnt] += s[i]
            if inc == True:
                cnt += 1
            else:
                cnt -=1
            if cnt == numRows:
                inc = False
            elif cnt == 1:
                inc = True
            i +=1
        
        for k in range(1, numRows+1):
            ret_str += str_dict[k]
        return ret_str
        
