class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0: 
            return False
        start = int(math.floor(math.sqrt(num)))
        if num == start**2: 
            arr = [1, start]
            temp = start - 1
            pass
        else: 
            arr = [1]
            temp = start
            pass
        while temp > 1: 
            if num%temp == 0: 
                arr.append(temp)
                arr.append(num/temp)
                pass
            temp -= 1
            pass
        #print arr
        if num == sum(arr): 
            return True
        else: 
            return False
        pass
