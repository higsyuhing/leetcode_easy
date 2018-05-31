class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1: 
            return x
        i = 1
        j = x
        while (j - i > 1): 
            #print "1: ", i, j
            k = (i + j)/2
            temp = k * k
            if temp > x: 
                j = k
                pass
            else: 
                i = k
                pass
            #print "2: ", i, j
            pass
        return i
                
