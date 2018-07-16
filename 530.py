# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # traverse in order, then all distance must be in neighbor
        old = None
        dis = -1
        stack = []
        temp = root
        while 1: 
            if temp != None: 
                stack.append(temp)
                temp = temp.left
                pass
            else: 
                if len(stack) > 0: 
                    temp = stack.pop()
                    if old != None: 
                        if dis == -1:
                            dis = abs(temp.val - old.val)
                            pass
                        else:
                            dis = min(dis, abs(temp.val - old.val))
                            pass
                        pass
                    old = temp
                    temp = temp.right
                    pass
                else: 
                    break
                    pass
                pass
            pass
        return dis
