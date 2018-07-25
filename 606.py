# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def func(self, node): 
        if node == None: 
            return ""
        if node.left == None and node.right == None: 
            return str(node.val)
        if node.right == None: 
            str1 = self.func(node.left)
            return str(node.val) + "(" + str1 + ")"
        str1 = self.func(node.left)
        str2 = self.func(node.right)
        return str(node.val) + "(" + str1 + ")(" + str2 + ")"
    
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        return self.func(t)
        
        
