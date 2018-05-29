class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0: 
            temp = x
            pass
        else: 
            temp = -x
            pass
        res = 0
        while temp > 0: 
            res = res*10 + temp%10
            temp = temp/10
            pass
        if x < 0:
            res = -res
            pass
        if res < -2**31:
            return 0
        if res > (2**31-1): 
            return 0
        return res
        
        
