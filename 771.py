class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        dic = {}
        for char in J: 
            dic[char] = 1
            pass
        res = 0
        for char in S: 
            if dic.has_key(char): 
                res += 1
                pass
            pass
        return res
