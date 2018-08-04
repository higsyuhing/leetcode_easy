# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # master function: the node is the leader of this branch
    # retrun the max length under this node (maynot be the val of this node)
    def func1(self, node): 
        if node.left == None and node.right == None: 
            return 0
        elif node.left != None and node.right == None: 
            leftret = self.func2(node.left, node.val)
            return max(leftret[0], leftret[1], leftret[2])
        elif node.left == None and node.right != None: 
            rightret = self.func2(node.right, node.val)
            return max(rightret[0], rightret[1], rightret[2])
        else: 
            leftret = self.func2(node.left, node.val)
            rightret = self.func2(node.right, node.val)
            thislen = leftret[0] + rightret[0]
            return max(thislen, leftret[1], rightret[1], leftret[2], rightret[2])
        pass
    
    # slave function: the node should be same value for its leader
    # return [max single length for this val, max contained length for this val, the max length for all other val]
    def func2(self, node, val): 
        # never be a None node
        if node.val != val: 
            # this node will be a new branch and has no contribution to val
            return [0, 0, self.func1(node)]
        # same val
        if node.left == None and node.right == None: 
            # the leaf node, 
            # 1 for connecting to parent, 0 for no contained length, 0 for no others
            return [1, 0, 0]
        elif node.left != None and node.right == None: 
            leftret = self.func2(node.left, node.val)
            # left node will + 1 for single length, no right child, so no contained length change, no others
            return [leftret[0]+1, leftret[1], leftret[2]]
        elif node.left == None and node.right != None: 
            rightret = self.func2(node.right, node.val)
            # same as left
            return [rightret[0]+1, rightret[1], rightret[2]]
        else: 
            leftret = self.func2(node.left, node.val)
            rightret = self.func2(node.right, node.val)
            singlelen = max(leftret[0], rightret[0]) + 1
            containedlen = max(leftret[0] + rightret[0], leftret[1], rightret[1])
            otherlen = max(leftret[2], rightret[2])
            return [singlelen, containedlen, otherlen]
        pass
    
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: 
            return 0
        return self.func1(root)
