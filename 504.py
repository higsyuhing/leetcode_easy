class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: 
            return "0"
        negflag = False
        realnum = num
        if num < 0: 
            negflag = True
            realnum = -num
            pass
        arr = []
        while realnum > 0: 
            arr.append(str(realnum%7))
            realnum = realnum/7
            pass
        arr.reverse()
        if negflag: 
            return ("-"+"".join(arr))
        else: 
            return "".join(arr)
        pass
