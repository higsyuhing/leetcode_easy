class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = []
        for index in range(rowIndex+1): 
            temp = [1]
            for i in range(index): 
                if i == index - 1: 
                    temp.append(1)
                    pass
                else: 
                    temp.append(res[i] + res[i+1])
                    pass
                pass
            res = temp
            pass
        return res
