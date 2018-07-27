class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        for index in range(len(nums)): 
            dic[index+1] = 1
            pass
        res = [-1, -1]
        for num in nums: 
            if dic.has_key(num): 
                del dic[num]
                pass
            else: 
                res[0] = num
                pass
            pass
        arr = dic.items()
        res[1] = arr[0][0]
        return res
        
