# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        temp = root
        stack = []
        node = None # current common ancestor
        progress = 0 # current progress
        while 1: 
            if temp != None: 
                stack.append(temp)
                temp = temp.left
                pass
            else: 
                if len(stack) == 0: 
                    break
                    pass
                else: 
                    temp = stack.pop()
                    if temp == node: 
                        temp = stack.pop()
                        node = temp
                        stack.append(node)
                        pass
                    if temp == p or temp == q: 
                        if progress == 0: 
                            node = temp
                            stack.append(node)
                            progress = 1
                            pass
                        else: 
                            return node
                        pass
                    #print temp.val, progress, node
                    temp = temp.right
                    pass
                pass
            pass
        print "Cannot find! "
        return None
        
        
