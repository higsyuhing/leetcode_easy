class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = list(nums)
        arr.sort()
        start = -1
        end = len(arr)
        for index in range(end): 
            if nums[index] != arr[index]: 
                start = index
                break
                pass
            pass
        #print start
        if start == -1: # all same
            return 0
        for index in range(end): 
            if nums[end - 1 - index] != arr[end - 1 - index]: 
                end = end - index
                break
                pass
            pass
        return (end - start)
