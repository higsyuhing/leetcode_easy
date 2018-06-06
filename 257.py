# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def func(self, node, stack, res): 
        if node.left == None and node.right == None: 
            stack.append(str(node.val))
            res.append("->".join(stack))
            stack.pop()
            return res
        if node.left != None and node.right == None: 
            stack.append(str(node.val))
            res = self.func(node.left, stack, res)
            stack.pop()
            return res
        if node.left == None and node.right != None: 
            stack.append(str(node.val))
            res = self.func(node.right, stack, res)
            stack.pop()
            return res
        # else
        stack.append(str(node.val))
        res = self.func(node.left, stack, res)
        res = self.func(node.right, stack, res)
        stack.pop()
        return res
    
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None: 
            return []
        return self.func(root, [], [])
