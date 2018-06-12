class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0: 
            return False
        temp = 0
        index = 1
        while 1: 
            if num == temp: 
                return True
            if num < temp: 
                return False
            temp += index
            index += 2
            pass
        pass
