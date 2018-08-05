# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def func(self, node, val): 
        if node == None: 
            return None
        # test first, find the earliest one
        if node.val == val: 
            return node
        if node.val > val: 
            return self.func(node.left, val)
        else: 
            return self.func(node.right, val)
        pass
        
        
    
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        return self.func(root, val)
