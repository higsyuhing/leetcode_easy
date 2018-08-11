class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        gap = 0
        last = -1
        index = 0
        temp = N
        while temp > 0: 
            curr = temp%2
            temp = temp/2
            if curr == 1: 
                if last == -1: 
                    last = index
                    pass
                else: 
                    gap = max(gap, index - last)
                    last = index
                    pass
                pass
            index += 1
            pass
        return gap
