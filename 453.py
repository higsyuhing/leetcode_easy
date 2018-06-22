class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # increase n-1 elements by 1 => decrease 1 element
        # i.e. find the sum above the smallest element
        arr_sum = 0
        arr_min = nums[0]
        for num in nums: 
            arr_sum += num
            if arr_min > num: 
                arr_min = num
                pass
            pass
        return (arr_sum - arr_min*len(nums))
