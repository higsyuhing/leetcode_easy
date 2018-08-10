class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []
        rlen = len(A)
        clen = len(A[0])
        for i in range(rlen): 
            arr = []
            for j in range(clen): 
                jj = clen - 1 - j
                temp = A[i][jj]
                arr.append(1 - temp)
                pass
            ret.append(arr)
            pass
        return ret
                
