class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # you can use math function log2 and check odd/even
        # but they are pretty same... 
        if num <= 0: 
            return False
        temp = num
        index = 0
        while temp & 0x1 == 0: 
            temp = temp >> 1
            index += 1
            pass
        if temp != 1: 
            return False
        else: 
            if index%2 == 0: 
                return True
            else: 
                return False
            pass
        pass
