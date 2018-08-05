class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # this has a pretty bad performance
        dic = {}
        for num in nums: 
            if dic.has_key(num): 
                dic[num] += 1
                pass
            else: 
                dic[num] = 1
                pass
            pass
        arr = dic.items()
        maxp = 0
        for item in arr: 
            if item[1] > maxp: 
                maxp = item[1]
                pass
            pass
        target = []
        for item in arr: 
            if item[1] == maxp: 
                target.append(item[0])
                pass
            pass
        res = []
        for ele in target: 
            i = 0
            j = len(nums) - 1
            while 1: 
                if nums[i] == ele: 
                    break
                    pass
                i += 1
                pass
            while 1: 
                if nums[j] == ele: 
                    break
                    pass
                j -= 1
                pass
            res.append((j + 1 - i))
            pass
        return min(res)
        
        
        
        
        
