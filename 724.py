class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summ = sum(nums)
        left = 0
        temp = 0
        right = summ
        for i in range(len(nums)): 
            left += temp
            temp = nums[i]
            right -= temp
            if left == right: 
                return i
            pass
        return -1
        
