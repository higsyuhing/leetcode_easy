# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def func(self, node, sum_target, sum_temp): 
        # node is not None
        sum_temp = sum_temp + node.val
        if node.left == None and node.right == None: 
            if sum_temp == sum_target: 
                return True
            else: 
                return False
            pass
        ret1 = False
        ret2 = False
        if node.right != None: 
            ret1 = self.func(node.right, sum_target, sum_temp)
            pass
        if node.left != None: 
            ret2 = self.func(node.left, sum_target, sum_temp)
            pass
        return (ret1 or ret2)
    
    def hasPathSum(self, root, sum_target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None: 
            return False
        return self.func(root, sum_target, 0)
