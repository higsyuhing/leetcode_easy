class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dic = {}
        for index in range(len(nums)): 
            if nums[index] < target: 
                if nums[index] in num_dic: 
                    pass
                else: 
                    num_dic[nums[index]] = index
                    pass
                cor_val = target - nums[index]
                if cor_val in num_dic: 
                    return [num_dic[cor_val], index]
                pass
            pass
        return []
    
