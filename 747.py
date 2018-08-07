class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: 
            return 0
        findex = -1
        first = -1
        sindex = -1
        second = -1
        for index in range(len(nums)): 
            if findex == -1: 
                findex = index
                first = nums[findex]
                pass
            else: 
                if nums[index] > first: 
                    second = first
                    sindex = 1
                    first = nums[index]
                    findex = index
                    pass
                else: 
                    if sindex == -1: 
                        sindex = 1
                        second = nums[index]
                        pass
                    elif second < nums[index]:
                        second = nums[index]
                        pass
                    pass
                pass
            pass
        if first >= 2*second: 
            return findex
        else: 
            return -1
        pass
                        
        
