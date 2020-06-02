class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        a, b, diff = set(A),set(B), (sum(A)-sum(B))//2
        
        for i in a:
            if i - diff in b:
                return [i, i-diff]
