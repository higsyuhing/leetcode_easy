# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def func(self, node): 
        # node != None
        if node.left == None and node.right == None: 
            return 1
        elif node.left == None and node.right != None: 
            return (self.func(node.right) + 1)
        elif node.left != None and node.right == None: 
            return (self.func(node.left) + 1)
        else: 
            dep1 = (self.func(node.left) + 1)
            dep2 = (self.func(node.right) + 1)
            return min(dep1, dep2)
        pass
    
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: 
            return 0
        return self.func(root)
