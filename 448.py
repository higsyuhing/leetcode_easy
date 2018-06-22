class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for i in range(len(nums)): 
            arr.append(0)
            pass
        for num in nums: 
            arr[num-1] += 1
            pass
        res = []
        for index in range(len(arr)): 
            if arr[index] == 0: 
                res.append((index+1))
                pass
            pass
        return res
