class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # wtf this problem... 
        p = None
        for i in xrange(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if p is not None:
                    return False
                p = i

        return (p is None or p == 0 or p == len(nums)-2 or
                nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2])
