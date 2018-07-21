class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        # [0,0] is always the max num, but how many. 
        if len(ops) == 0: 
            return (m*n)
        min0 = ops[0][0]
        min1 = ops[0][1]
        for op in ops: 
            if op[0] < min0: 
                min0 = op[0]
                pass
            if op[1] < min1: 
                min1 = op[1]
                pass
            pass
        return (min0*min1)
