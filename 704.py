class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = -1
        end = len(nums)
        while (end - start) > 1: 
            mid = (start + end)/2
            if nums[mid] < target: 
                start = mid
                pass
            elif nums[mid] > target: 
                end = mid
                pass
            else: 
                return mid
            pass
        return -1
        
        
