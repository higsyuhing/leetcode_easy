class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        x = int(math.sqrt(c))
        while x >= 0: 
            ys = 2*c - x*x
            y = int(math.sqrt(ys))
            #print x, y
            if ys == y*y and (y-x)%2 == 0: 
                return True
            x -= 1
            pass
        return False
