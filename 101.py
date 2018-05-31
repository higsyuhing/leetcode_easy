# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkTree(self, leftnode, rightnode): 
        if leftnode == None and rightnode == None: 
            return True
        if leftnode == None and rightnode != None: 
            return False
        elif leftnode != None and rightnode == None: 
            return False
        elif leftnode.val != rightnode.val: 
            return False
        elif not self.checkTree(rightnode.left, leftnode.right): 
            return False
        elif not self.checkTree(leftnode.left, rightnode.right): 
            return False
        else: 
            return True
        pass
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: 
            return True
        return self.checkTree(root.left, root.right)        
            
