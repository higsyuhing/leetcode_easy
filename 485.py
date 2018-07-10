class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        temp = 0
        flag = False
        for ele in nums: 
            if ele: 
                if flag: 
                    temp += 1
                    pass
                else: 
                    flag = True
                    temp = 1
                    pass
                pass
            else: 
                if flag: 
                    if temp > count: 
                        count = temp
                        pass
                    temp = 0
                    flag = False
                    pass
                pass
            pass
        if temp > count: 
            count = temp
            pass
        return count
