class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        length = len(nums)
        if length <= 1: 
            return length
        for j in range(length-1): 
            curr = j + 1
            if nums[i] == nums[curr]: 
                pass
            else: 
                i = i + 1
                nums[i] = nums[curr]
                pass
            pass
        return i+1
