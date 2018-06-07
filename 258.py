class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # this can be solver by digital root
        # https://en.wikipedia.org/wiki/Digital_root
        # return 1 + (num-1)%9
        number = num
        while 1: 
            temp = number
            number = 0
            while temp > 0: 
                number += temp%10
                temp = temp/10
                pass
            if number < 10: 
                return number
            pass
        pass
