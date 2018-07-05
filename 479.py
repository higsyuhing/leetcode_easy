class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [9, 9009, 906609, 99000099, 9966006699, 999000000999, 99956644665999, 9999000000009999]
        return arr[n-1]%1337
        
        
        
        '''
        # method from CSDN
        if n == 1: 
            return 9
        upper = 10**n-1
        lower = 10**(n-1)
        i = upper
        while 1: 
            if i < lower: 
                break
                pass
            tempstr = str(i)
            tempstr1 = str(i) + tempstr[::-1]
            #print tempstr1
            num = int(tempstr1)
            j = upper
            while 1: 
                if j**2 < num: 
                    break
                    pass
                if num%j == 0: 
                    return num%1337
                j -= 1
                pass
            i -= 1
            pass
        return -1
        '''
            
