class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        table = {}
        for num in nums: 
            if table.has_key(num): 
                return True
            table[num] = 0
            pass
        return False
