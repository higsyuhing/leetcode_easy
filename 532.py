class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0: 
            return 0
        nums.sort()
        arr = []
        if k == 0: 
            curr = 0
            flag = False
            res = 0
            for index in range(len(nums)): 
                if index == 0 or nums[index-1] != nums[index]: 
                    curr = index
                    flag = False
                    pass
                elif nums[index] == nums[curr] and flag == False: 
                    flag = True
                    res += 1
                    pass
                pass
            return res
        for index in range(len(nums)): 
            if index == 0 or nums[index-1] != nums[index]: 
                arr.append(nums[index])
                pass
            pass
        #print arr
        queue = []
        res = 0
        # I like this, this is smart hahaha
        for num in arr: 
            while len(queue) > 0: 
                if queue[0] > num: 
                    break
                    pass
                if queue[0] == num: 
                    res += 1
                    pass
                del queue[0]
                pass
            queue.append(num + k)
            pass
        return res
