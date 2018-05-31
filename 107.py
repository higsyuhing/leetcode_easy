# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def func(self, node, depth, array): 
        if node == None: 
            return array
        if depth > len(array): 
            print "Error! "
            return array
        if depth == len(array): 
            array.append([node.val])
            pass
        else: 
            array[depth].append(node.val)
            pass
        array = self.func(node.left, depth + 1, array)
        return self.func(node.right, depth + 1, array)
    
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        array = self.func(root, 0, [])
        res = []
        while len(array) > 0: 
            res.append(array.pop())
            pass
        return res
