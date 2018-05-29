class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dic = {}
        for index in range(len(nums)): 
            cor_val = target - nums[index]
            if cor_val in num_dic: 
                return [num_dic[cor_val], index]
            if nums[index] in num_dic: 
                pass
            else: 
                num_dic[nums[index]] = index
                pass
            pass
        return []
    
    '''
    this can be done by many other ways, like: 
    - brute force: 2 nested loop
    - sorted array with 2 pointers
    '''
    
