class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        #return [0, 0]
        temp = int(math.sqrt(area))
        while 1: 
            if area%temp == 0: 
                return [area/temp, temp]
                pass
            temp -= 1
            pass
        pass
        
