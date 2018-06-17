# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def func(self, node, flag): 
        if node.left == None and node.right == None: 
            if flag == 0: 
                return node.val
            else: 
                return 0
            pass
        elif node.left == None and node.right != None: 
            return self.func(node.right, 1)
        elif node.left != None and node.right == None: 
            return self.func(node.left, 0)
        else: 
            return self.func(node.left, 0) + self.func(node.right, 1)
        pass
    
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: 
            return 0
        return self.func(root, 1)
