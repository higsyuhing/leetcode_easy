# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = -1 #undefined
        
        # get high
        temp = 1
        while guess(temp) > 0: 
            low = temp
            temp = temp << 1
            pass
        if guess(temp) == 0: 
            return temp
        else: 
            high = temp
            pass
        
        # guess number
        while 1: 
            mid = (low + high)/2
            res = guess(mid)
            if res == 0: 
                return mid
            elif res < 0: 
                high = mid
                pass
            else: 
                low = mid
                pass
            pass
        pass
