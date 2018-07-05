class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        p = 2 # 2^0
        while num >= p: 
            p = p << 1
            pass
        return p - 1 - num
