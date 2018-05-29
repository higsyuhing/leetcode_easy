class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for index in range(len(nums)): 
            if nums[index] == target: 
                return index
            elif nums[index] < target: 
                pass
            else: 
                index = index - 1
                break
                pass
            pass
        return index + 1
