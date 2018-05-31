# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def func(self, nums, i, j): 
        if i >= j: 
            return None
        mid = (i + j)/2
        node = TreeNode(nums[mid])
        node.left = self.func(nums, i, mid)
        node.right = self.func(nums, mid + 1, j)
        return node
    
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.func(nums, 0, len(nums))
