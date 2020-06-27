class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = []
        for i in range(0,n):
            memo.append(None)
        return self.climb(0, n, memo)
   
    def climb(self, i, n, memo):
        if i > n:
            return 0 #invalid path
        if i == n:
            return 1 #found vaild path
        if memo[i] > 0: #if already calculated
            return memo[i]
        memo[i] = self.climb(i+1, n, memo) + self.climb(i+2, n , memo) #calculate, add possible branches
        return memo[i]
