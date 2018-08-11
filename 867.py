class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for num in A[0]: 
            res.append([num])
            pass
        for ti in range(len(A) - 1): 
            i = ti + 1
            for j in range(len(A[0])): 
                res[j].append(A[i][j])
                pass
            pass
        return res
