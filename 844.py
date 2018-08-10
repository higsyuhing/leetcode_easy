class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        # reverse method is better. i.e. 2 pointers
        newS = []
        for char in S: 
            if char != "#": 
                newS.append(char)
                pass
            else: 
                if len(newS) > 0: 
                    newS.pop()
                    pass
                pass
            pass
        newT = []
        for char in T: 
            if char != "#":
                newT.append(char)
                pass
            else: 
                if len(newT) > 0: 
                    newT.pop()
                    pass
                pass
            pass
        if len(newS) != len(newT): 
            return False
        else: 
            for i in range(len(newS)): 
                if newS[i] != newT[i]: 
                    return False
                pass
            pass
        return True
