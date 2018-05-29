class Solution(object):
    def getNext(self, string): 
        # get the next count and say string, not use this function
        oldchar = None
        currnum = 0
        resstr = []
        for char in string: 
            if char != oldchar: 
                if oldchar != None: 
                    resstr = resstr + [str(currnum), oldchar]
                    pass
                oldchar = char
                currnum = 1
                pass
            else: 
                currnum = currnum + 1
                pass
            pass
        resstr = resstr + [str(currnum), oldchar]
        return ''.join(resstr)
    
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = "1"
        for i in range(n-1):
            # string = self.getNext(string)
            oldchar = None
            currnum = 0
            resstr = []
            for char in string: 
                if char != oldchar: 
                    if oldchar != None: 
                        resstr = resstr + [str(currnum), oldchar]
                        pass
                    oldchar = char
                    currnum = 1
                    pass
                else: 
                    currnum = currnum + 1
                    pass
                pass
            resstr = resstr + [str(currnum), oldchar]
            string = ''.join(resstr)
            pass
        return string
