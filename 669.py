# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def func(self, node, L, R): 
        if node == None: 
            return None
        if node.val < L: 
            return self.func(node.right, L, R)
        if node.val > R: 
            return self.func(node.left, L, R)
        # L <= val <= R
        cur = TreeNode(node.val)
        cur.left = self.func(node.left, L, R)
        cur.right = self.func(node.right, L, R)
        return cur
    
    
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        # will copy the tree, not modify it. 
        return self.func(root, L, R)
