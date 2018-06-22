class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = (math.sqrt(8*n+1)-1)/2
        return int(temp)
