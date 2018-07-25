# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def func(self, node1, node2): 
        if node1 == None and node2 == None: 
            return None
        if node1 != None and node2 == None: 
            resnode = TreeNode(node1.val)
            resnode.left = self.func(node1.left, None)
            resnode.right = self.func(node1.right, None)
            return resnode
        if node1 == None and node2 != None: 
            resnode = TreeNode(node2.val)
            resnode.left = self.func(None, node2.left)
            resnode.right = self.func(None, node2.right)
            return resnode
        resnode = TreeNode(node1.val + node2.val)
        resnode.left = self.func(node1.left, node2.left)
        resnode.right = self.func(node1.right, node2.right)
        return resnode
        
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        return self.func(t1, t2)
