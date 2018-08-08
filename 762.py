class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        # log2(10**6) is around 20), then just less than 20 dic
        dic = {0:0, 1:0, 2:1, 3:1, 4:0, 5:1, 6:0, 7:1, 8:0, 9:0, 10:0, 11:1, 12:0, 13:1, 14:0, 15:0, 16:0, 17:1, 18:0, 19:1, 20:0}
        res = 0
        num = L
        while num <= R: 
            count = 0
            temp = num
            while temp > 0: 
                count += temp%2
                temp = temp/2
                pass
            if dic[count] == 1: 
                res += 1
                pass
            num += 1
            pass
        return res
        
        
        
