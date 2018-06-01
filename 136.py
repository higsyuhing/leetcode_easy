class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # also hash table can do it, but requires extra memory
        # make set approach is compliex (hide in function "set")
        temp = 0
        for num in nums: 
            temp = temp ^ num
            pass
        return temp
