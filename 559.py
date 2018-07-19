"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def func(self, node): 
        if node == None: 
            return 0
        depth = 0
        for child in node.children: 
            depth = max(depth, self.func(child))
            pass
        return depth + 1
    
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        return self.func(root)
