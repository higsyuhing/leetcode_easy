class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        dic = {}
        for num in candies: 
            if not dic.has_key(num): 
                dic[num] = 1
                pass
            pass
        have = len(candies)/2
        kind = len(dic)
        if kind >= have: 
            return have
        else: 
            return kind
        pass
