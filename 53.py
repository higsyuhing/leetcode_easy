class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        queue_sum = nums[0]
        Max = nums[0]
        for index in range(len(nums)-1): 
            curr = index + 1
            if queue_sum < 0:
                queue_sum = nums[curr]
                pass
            else: 
                queue_sum = queue_sum + nums[curr]
                pass
            if queue_sum > Max: 
                Max = queue_sum
                pass
            pass
        return Max 


'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        queue = [nums[0]]
        queue_sum = nums[0]
        Max = nums[0]
        for index in range(len(nums)-1): 
            curr = index + 1
            if queue_sum < 0: 
                queue = [nums[curr]]
                queue_sum = nums[curr]
                pass
            else: 
                queue = queue + [nums[curr]]
                queue_sum = queue_sum + nums[curr]
                pass
            if queue_sum > Max: 
                Max = queue_sum
                pass
            pass
        return Max
'''
        
