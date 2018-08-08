# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        temp = root
        stack = []
        arr = []
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
        res = 10000000
        for i in range(len(arr) - 1): 
            res = min(res, arr[i+1] - arr[i])
        return res
        
        
