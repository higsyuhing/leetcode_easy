class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        target = length*(length+1)/2
        temp = 0
        for num in nums: 
            temp += num
            pass
        return (target-temp)
