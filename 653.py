# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        stack = []
        arr = []
        temp = root
        while 1: 
            if temp != None: 
                stack.append(temp)
                temp = temp.left
                pass
            else: 
                if len(stack) > 0: 
                    temp = stack.pop()
                    
                    #print arr
                    curr = temp.val
                    target = k - curr
                    while len(arr) > 0 and curr > arr[-1]: 
                        arr.pop()
                        pass
                    if len(arr) > 0 and curr == arr[-1]: 
                        return True
                    if target >= curr: 
                        arr.append(target)
                        pass
                    
                    temp = temp.right
                    pass
                else: 
                    break
                    pass
                pass
            pass
        return False
        
        
