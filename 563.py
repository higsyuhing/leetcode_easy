# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def func(self, node): 
        # return [sumtile, tsum]
        if node == None: 
            return [0, 0]
        ret1 = self.func(node.left)
        ret2 = self.func(node.right)
        sumtile = ret1[0] + ret2[0] + abs(ret1[1] - ret2[1])
        tsum = ret1[1] + ret2[1] + node.val
        return [sumtile, tsum]
    
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = self.func(root)
        return ret[0]
