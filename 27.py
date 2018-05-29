class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j in nums: 
            if j == val: 
                pass
            else: 
                nums[i] = j
                i = i + 1
                pass
            pass
        return i
