class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # the non-recursion/loop solution is borning. 
        # I think the Binomial coefficient is related with this problem
        if n <= 0: 
            return False
        temp = n
        while temp%3 == 0: 
            temp = temp / 3
            pass
        if temp == 1: 
            return True
        else: 
            return False
