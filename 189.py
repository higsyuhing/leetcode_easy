class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        array = []
        alen = len(nums)
        k = k%alen
        if k == 0: 
            return
        for index in range(k): 
            array.append(nums[index%alen])
            pass
        for index in range(alen): 
            targetindex = (index + k)%alen
            arrayindex = index%k
            temp = nums[targetindex]
            nums[targetindex] = array[arrayindex]
            array[arrayindex] = temp
            pass
        return
                
        
        
        '''
        alen = len(nums)
        while k > 0: 
            temp = nums[alen - 1]
            for index in range(alen-1): 
                curr = alen - 2 - index
                nums[curr + 1] = nums[curr]
                pass
            nums[0] = temp
            k = k - 1
            pass
        return
        '''
            
