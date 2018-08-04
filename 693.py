class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = n
        while temp > 0: 
            if ((temp & 0x1)*2) == (temp & 0x2): 
                return False
            temp = temp >> 1
            pass
        return True
