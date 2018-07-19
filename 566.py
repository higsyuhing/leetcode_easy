class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        orir = len(nums)
        oric = len(nums[0])
        if orir*oric != r*c or not (orir and oric): 
            return nums
        tempr = 0
        tempc = 0
        ret = []
        for indexi in range(r): 
            row = []
            for indexj in range(c): 
                row.append(nums[tempr][tempc])
                tempc += 1
                if tempc == oric: 
                    tempc = 0
                    tempr += 1
                    pass
                pass
            ret.append(row)
            pass
        return ret
            
