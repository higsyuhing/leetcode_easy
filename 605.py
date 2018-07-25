class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        left = -1
        index = 0
        length = len(flowerbed)
        while index < length: 
            if flowerbed[index] == 1: 
                right = index - 1
                #print left, right
                if left + 1 < right: 
                    count += (right - left)/2
                    pass
                left = index + 1
                pass
            index += 1
            pass
        right = length
        #print left, right
        if left + 1 < right: 
            count += (right - left)/2
            pass
        return (n <= count)
    
