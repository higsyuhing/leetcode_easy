class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        last = S[0]
        lastindex = 0
        res = []
        for index in range(len(S)): 
            char = S[index]
            if char != last: 
                if (index - lastindex) >= 3: 
                    temparr = [lastindex, index - 1]
                    res.append(temparr)
                    pass
                last = char
                lastindex = index
                pass
            pass
        if (len(S) - lastindex) >= 3: 
            temparr = [lastindex, len(S) - 1]
            res.append(temparr)
            pass
        return res
                
