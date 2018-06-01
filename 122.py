class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1: 
            return 0
        temp = prices[0]
        Max = 0
        for index in range(len(prices)-1): 
            curr = index + 1
            if prices[curr] - temp > 0: 
                Max = Max + prices[curr] - temp
                pass
            temp = prices[curr]
            pass
        return Max
        
        
