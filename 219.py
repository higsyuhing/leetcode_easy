class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        k = k + 1
        table = {}
        if k >= len(nums): 
            for num in nums: 
                if table.has_key(num): 
                    return True
                table[num] = 0
                pass
            return False
        for index in range(k): 
            if table.has_key(nums[index]): 
                return True
            table[nums[index]] = 0
            pass
        for index in range(len(nums) - k): 
            del table[nums[index]]
            curr = index + k
            if table.has_key(nums[curr]): 
                return True
            table[nums[curr]] = 0
            pass
        return False
        
