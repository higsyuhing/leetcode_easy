class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0: 
            return ''
        temp = n
        res = ''
        while temp > 0: 
            res = chr(65 + (temp-1)%26) + res
            temp = (temp-1)/26
            pass
        return res
