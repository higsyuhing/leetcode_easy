class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        curr = 0
        target = 0
        while curr < len(nums): 
            if nums[curr] != 0: 
                if curr != target: 
                    nums[target] = nums[curr]
                    nums[curr] = 0
                    pass
                target += 1
                pass
            curr += 1
            pass
        return
