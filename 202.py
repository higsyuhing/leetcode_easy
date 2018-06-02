class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = 0
        temp = n
        while 1: 
            # but why is 4?? 
            if temp == 4: 
                return False
            Sum = 0
            while temp > 0: 
                Sum = Sum + (temp%10)**2
                temp = temp/10
                pass
            if Sum == 1: 
                return True
            else: 
                temp = Sum
                pass
            count = count + 1
            if count == 50: 
                break
            pass      
        return False
