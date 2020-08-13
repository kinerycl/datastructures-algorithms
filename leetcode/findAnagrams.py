class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        #create dictionary of ALL lower alpha
        p_counts = dict()
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        for char in alpha:
            p_counts[char] = 0
        
        #populate
        for char in p:
            p_counts[char]+=1
                
        ret_lst = []
        left, right =  0,0
        count = len(p)
        while right <len(s):
            if p_counts[s[right]] >= 1:
                count -=1
            p_counts[s[right]]-=1
            right+=1
            
            if count == 0:
                ret_lst.append(left)
            
            if right-left == len(p):
                if p_counts[s[left]] >=0:
                    count +=1
                p_counts[s[left]]+=1
                left+=1

        return ret_lst
