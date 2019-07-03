class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        for i in range(numRows):
            if i == 0: #inital
                ret.append([1])
            else:      #build inner list
                app = []
                for j in range(len(ret[i-1])+1): #previous
                    if j == 0 or j == len(ret[i-1]): #edges
                        app.append(1)
                    else:
                        app.append(ret[i-1][j]+ret[i-1][j-1])
                ret.append(app)
        return ret
