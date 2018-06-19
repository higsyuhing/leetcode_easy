class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        state = 0 # 0: space char, 1: non-space char
        for char in s: 
            if char == ' ' and state == 1: 
                res += 1
                state = 0
                pass
            if char != ' ' and state == 0: 
                state = 1
                pass
            pass
        if state == 1: 
            return res+1
        else: 
            return res
        pass
                
