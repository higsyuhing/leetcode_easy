class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        flag = False # before mountain, True after mountain
        last = -1
        ret = -1
        for index in range(len(A)): 
            num = A[index]
            if num < last: 
                return index - 1
            last = num
            pass
        return (len(A) - 1)
    
    
