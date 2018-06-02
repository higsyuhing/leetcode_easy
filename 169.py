class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Boyer-Moore Voting Algorithm, smart!
        candidate = 0
        count = 0
        for num in nums: 
            if count == 0: 
                candidate = num
                count = 1
                pass
            else: 
                if candidate == num: 
                    count = count + 1
                    pass
                else: 
                    count = count - 1
                    pass
                pass
            pass
        return candidate
        
        '''
        nums.sort()
        return nums[len(nums)/2]
        '''
