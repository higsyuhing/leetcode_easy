class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: 
            return 0
        ret = 0
        count = 0
        last = nums[0]
        for num in nums: 
            if num > last: 
                count += 1
                last = num
                pass
            else:
                ret = max(ret, count)
                count = 1
                last = num
                pass
            pass
        return max(ret, count)
            
                
