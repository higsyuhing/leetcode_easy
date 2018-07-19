class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)%2 != 0: 
            print "Error: need even numbers"
            return 0
        nums.sort()
        ret = 0
        for index in range(len(nums)/2): 
            temp = index*2
            ret += nums[temp]
            pass
        return ret
