# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        arr1 = []
        stack = []
        temp = root1
        while 1: 
            if temp != None: 
                stack.append(temp)
                temp = temp.left
                pass
            else: 
                if len(stack) > 0: 
                    temp = stack.pop()
                    if temp.left == None and temp.right == None: 
                        arr1.append(temp.val)
                        pass
                    temp = temp.right
                    pass
                else: 
                    break
                    pass
                pass
            pass
        #print arr1
        arr2 = []
        stack = []
        temp = root2
        while 1: 
            if temp != None: 
                stack.append(temp)
                temp = temp.left
                pass
            else: 
                if len(stack) > 0: 
                    temp = stack.pop()
                    if temp.left == None and temp.right == None: 
                        arr2.append(temp.val)
                        pass
                    temp = temp.right
                    pass
                else: 
                    break
                    pass
                pass
            pass
        #print arr2
        if len(arr1) != len(arr2): 
            return False
        for index in range(len(arr1)): 
            if arr1[index] != arr2[index]: 
                return False
            pass
        return True
                    
                    
                    
