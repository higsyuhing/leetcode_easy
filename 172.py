class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # the number of 2 is enough, so it depends on the number of 5
        res = 0
        temp = n
        while temp > 0: 
            res = res + temp/5
            temp = temp/5
            pass
        return res
