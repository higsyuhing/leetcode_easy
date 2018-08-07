class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        num = left
        while num <= right: 
            arr = []
            temp = num
            while temp > 0: 
                arr.append(temp%10)
                temp = temp/10
                pass
            flag = True
            for digit in arr: 
                if digit == 0: 
                    flag = False
                    break
                    pass
                if num%digit != 0: 
                    flag = False
                    break
                    pass
                pass
            if flag: 
                res.append(num)
                pass
            num += 1
            pass
        return res
