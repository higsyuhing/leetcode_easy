class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2: 
            return 0
        array = []
        for i in range(n-2): 
            array.append(0)
            pass
        # number is index + 2, index for array
        num = 0 # num of prime
        for index in range(n-2): 
            # print array
            curr = index + 2
            tempindex = index
            if array[tempindex] == 0: 
                num = num + 1
                while tempindex < (n-2): 
                    array[tempindex] = 1
                    tempindex = tempindex + curr
                    pass
                pass
            pass
        return num
