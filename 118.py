class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if numRows == 0: 
            return res
        for index in range(numRows): 
            temp = [1]
            for i in range(index): 
                if i == index - 1: 
                    temp.append(1)
                    pass
                else: 
                    temp.append(res[index-1][i] + res[index-1][i+1])
                    pass
                pass
            res.append(temp)
            pass
        return res
