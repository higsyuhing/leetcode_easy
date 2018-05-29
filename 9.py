class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        temp = x
        res = 0
        while temp > 0: 
            res = res*10 + temp%10
            temp = temp/10
            pass
        if res == x: 
            return True
        else: 
            return False
