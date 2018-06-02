class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: 
            return False
        temp = n
        while (temp%2 == 0): 
            temp = temp >> 1
            pass
        temp = temp >> 1
        if temp > 0: 
            return False
        else: 
            return True
