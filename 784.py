class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        arr = []
        base = []
        for index in range(len(S)): 
            char = S[index]
            if ord(char) > 64: 
                arr.append(index)
                if ord(char) < 96: 
                    char = chr(ord(char) + 32)
                    pass
                pass
            base.append(str(char))
            pass
        res = []
        arr.reverse()
        #print base, arr
        for i in range(2**len(arr)): 
            temp = list(base)
            index = i
            ii = 0
            while index > 0: 
                if index%2: 
                    temp[arr[ii]] = str(chr(ord(temp[arr[ii]])-32))
                    pass
                index = index/2
                ii += 1
                pass
            res.append("".join(temp))
            pass
        return res
            
            
            
