class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ret = []
        lets = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        for dig in digits:              #iterate through phone number
            if len(ret) == 0:           #initalizes list
                ret = list(lets[dig])
            else:
                end = len(ret)          #iterate through current list
                i = 0                   #just counter NOT index
                while i < end:
                    for letter in lets[dig]:    #iterate through potentials
                        ret.append(ret[0] + letter)
                    i += 1
                    ret.pop(0)             #remove letter
        return ret

