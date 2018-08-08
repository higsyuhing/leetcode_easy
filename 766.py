class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        dic = {}
        for i in range(len(matrix)): 
            for j in range(len(matrix[0])): 
                index = j - i
                temp = matrix[i][j]
                if dic.has_key(index): 
                    if dic[index] != temp: 
                        return False
                    pass
                else: 
                    dic[index] = temp
                    pass
                pass
            pass
        return True
        
