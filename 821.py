class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        # solution has the same meaning, but it's kind of opposite way, which is cheaper
        # use two "stacks"
        flast = -1
        farr = []
        blast = -1
        barr = []
        for i in range(len(S)): 
            # forward part
            findex = i
            if S[findex] != C: 
                if flast == -1: 
                    flast = findex
                    pass
                farr.append(1000000)
                pass
            else: 
                if flast != -1: 
                    tempindex = findex - 1
                    dis = 1
                    while tempindex >= flast: 
                        farr[tempindex] = dis
                        dis += 1
                        tempindex -= 1
                        pass
                    pass
                flast = -1
                farr.append(0)
                pass
            # backward part
            bindex = len(S) - 1 - i
            if S[bindex] != C: 
                if blast == -1: 
                    blast = findex
                    pass
                barr.append(1000000)
                pass
            else: 
                if blast != -1: 
                    tempindex = findex - 1
                    dis = 1
                    while tempindex >= blast: 
                        barr[tempindex] = dis
                        dis += 1
                        tempindex -= 1
                        pass
                    pass
                blast = -1
                barr.append(0)
                pass
            pass
        #print farr
        #print barr
        barr.reverse()
        ret = []
        for i in range(len(barr)): 
            temp = min(farr[i], barr[i])
            ret.append(temp)
            pass
        return ret
        
