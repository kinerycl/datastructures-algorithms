class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        cash = {5:0, 10:0, 20:0}
        for i in bills:
            cash[i] +=1
            
            if i == 5:
                continue
            elif (i == 10) and (cash[5]>0):
                cash[5]-=1
            elif (i ==20) and (cash[5]>0) and (cash[10]>0):
                cash[5]-=1
                cash[10]-=1
            elif (i ==20) and (cash[5]>=3):
                cash[5]-=3
            else:
                return False

        return True
