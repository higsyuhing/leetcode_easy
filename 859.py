class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B): 
            return False
        if len(A) <= 1: 
            return False
        diffarr = []
        for index in range(len(A)): 
            if A[index] != B[index]: 
                diffarr.append(index)
                pass
            pass
        if len(diffarr) > 2 or len(diffarr) == 1: 
            # 3 or more diffs, no chance to swap back
            # only 1 diff, no way to swap
            return False
        if len(diffarr) == 0: 
            # same string, then see if duplicate
            dic = {}
            for char in A: 
                if dic.has_key(char): 
                    return True
                dic[char] = 1
                pass
            return False
        # has 2 diffs
        pos0 = diffarr[0]
        pos1 = diffarr[1]
        if (A[pos0] == B[pos1]) and (A[pos1] == B[pos0]): 
            return True
        return False
        
        
