# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # traverse 2 times
        # stupid, use right iterative will be good! 
        arr = []
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
                    arr.append(temp.val)
                    temp = temp.right
                    pass
                else: 
                    break
                    pass
                pass
            pass
        count = sum(arr)
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
                    tempval = temp.val
                    temp.val = count
                    count -= tempval
                    temp = temp.right
                    pass
                else: 
                    break
                    pass
                pass
            pass
        return root
        
        
        
        
