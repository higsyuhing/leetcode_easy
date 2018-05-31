class Solution(object):    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # f(n) = f(n-1) + f(n-2)
        if n == 1 or n == 2: 
            return n
        a = 1
        b = 2
        for index in range(n-2): 
            temp = b
            b = a + b
            a = temp
            pass
        return b
