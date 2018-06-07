class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: 
            return False
        if num == 1: 
            return True
        temp = num
        while temp%2 == 0: 
            temp = temp/2
            pass
        while temp%3 == 0: 
            temp = temp/3
            pass
        while temp %5 == 0: 
            temp = temp/5
            pass
        if temp == 1: 
            return True
        else: 
            return False
        pass
