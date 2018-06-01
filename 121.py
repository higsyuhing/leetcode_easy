class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1: 
            return 0
        Max = 0
        Min = prices[0]
        for index in range(len(prices)-1): 
            curr = index + 1
            temp = prices[curr]
            if temp < Min: 
                Min = temp
                pass
            else: 
                if (temp - Min) > Max: 
                    Max = temp - Min
                    pass
                pass
            pass
        return Max
                
            
