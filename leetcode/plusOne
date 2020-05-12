class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        lead = 0 
        for i in range(len(digits)-1, -1, -1):
            lead = 0 
            if digits[i] + 1 == 10:
                digits[i] = 0
                lead = 1
            else:
                digits[i] = digits[i] +1
                break
        
        if lead == 1 :
            digits.insert(0, 1)
            
        return digits
