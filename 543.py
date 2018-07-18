# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def func(self, node):
        # return a list with 2 elements: 
        # [the longest path, the diameter from sub-node]
        if node.left == None and node.right == None: 
            return [0, 0]
        elif node.left != None and node.right != None: 
            res1 = self.func(node.left)
            res2 = self.func(node.right)
            retval1 = max(res1[0], res2[0]) + 1
            retval2 = max(res1[1], res2[1], res1[0] + res2[0] + 2)
            return [retval1, retval2]
        elif node.left != None and node.right == None: 
            res1 = self.func(node.left)
            retval1 = res1[0] + 1
            retval2 = max(res1[1], res1[0] + 1)
            return [retval1, retval2]
        else: # left == None and right != None
            res2 = self.func(node.right)
            retval1 = res2[0] + 1
            retval2 = max(res2[1], res2[0] + 1)
            return [retval1, retval2]
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: 
            return 0
        res = self.func(root)
        return res[1]
