class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = n
        level = 0 # 1 digit per num
        while 1: 
            boundary = 9*(level+1)*(10**level)
            if temp <= boundary: 
                break
                pass
            temp -= boundary
            level += 1
            pass
        if level == 0: 
            return temp
        temp -= 1
        pos = level - temp%(level+1)
        num = temp/(level+1) + 10**level
        #print level, temp, pos, num
        return (num/(10**pos))%10
        
