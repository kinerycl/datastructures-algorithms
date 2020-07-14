class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack= []
        out = [ 0 for i in range(len(T))]

        for i in range(len(T)-1, -1, -1):
            while stack and (T[i] >= stack[-1][0]):
                stack.pop()
            if stack:
                out[i] = stack[-1][1] - i     
            stack.append((T[i], i))
        return out
