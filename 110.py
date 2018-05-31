# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def func(self, node): 
        if node == None: 
            return [0, True]
        res1 = self.func(node.left)
        if res1[1] == False: 
            return res1
        res2 = self.func(node.right)
        if res2[1] == False: 
            return res2
        res = [max(res1[0], res2[0])+1]
        if res1[0] - res2[0] > 1 or res2[0] - res1[0] > 1: 
            res.append(False)
            pass
        else: 
            res.append(True)
            pass
        return res
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = self.func(root)
        return res[1]
