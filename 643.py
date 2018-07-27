class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        count = 0
        for index in range(k):
            count += nums[index]
            pass
        maxcount = count
        for index in range(len(nums) - k): 
            count += nums[index + k] - nums[index]
            if count > maxcount: 
                maxcount = count
                pass
            pass
        return float(maxcount)/float(k)
