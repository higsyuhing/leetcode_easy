class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.check = [0]
        temp = 0
        for num in nums: 
            temp += num
            self.check.append(temp)
            pass
        pass

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # Yeah, it's a smart method. Caching is just so so. 
        return self.check[j+1] - self.check[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
