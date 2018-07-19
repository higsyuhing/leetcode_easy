# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def test(self, node, t): 
        if node == None and t != None: 
            return False
        elif node != None and t == None: 
            return False
        elif node == None and t == None: 
            return True
        elif node.val != t.val: 
            return False
        else: 
            return self.test(node.left, t.left) and self.test(node.right, t.right)
    
    
    def func(self, node, t): 
        if node == None: 
            return False
        if self.test(node, t): 
            return True
        elif self.func(node.left, t): 
            return True
        else: 
            return self.func(node.right, t)
        pass
    
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.func(s, t)
