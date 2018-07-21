class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: 
            return 0
        dic = {}
        for num in nums: 
            if dic.has_key(num): 
                dic[num] += 1
            else: 
                dic[num] = 1
                pass
            pass
        arr = dic.items()
        arr.sort()
        #print arr
        # sort by key
        if len(arr) == 1: 
            return 0
        count = 0
        for index in range(len(arr) - 1): 
            if arr[index][0] + 1 == arr[index + 1][0]: 
                temp = arr[index][1] + arr[index+1][1]
                if temp > count: 
                    count = temp
                    pass
                pass
            pass
        return count
