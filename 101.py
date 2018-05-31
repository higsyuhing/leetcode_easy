# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: 
            return True
        stack1 = []
        stack2 = []
        temp1 = root.left
        temp2 = root.right
        while 1: 
            while 1: 
                if temp1 == None and temp2 == None: 
                    break
                    pass
                elif temp1 == None and temp2 != None: 
                    return False
                elif temp1 != None and temp2 == None: 
                    return False
                elif temp1.val != temp2.val: 
                    return False
                else: 
                    stack1.append(temp1)
                    stack2.append(temp2)
                    temp1 = temp1.left
                    temp2 = temp2.right
                    pass
                pass
            if len(stack1) > 0: 
                temp1 = stack1.pop()
                temp2 = stack2.pop()
                temp1 = temp1.right
                temp2 = temp2.left
                pass
            else: 
                return True


'''
class Solution(object):
    def checkTree(self, leftnode, rightnode): 
        if leftnode == None and rightnode == None: 
            return True
        if leftnode == None and rightnode != None: 
            return False
        elif leftnode != None and rightnode == None: 
            return False
        elif leftnode.val != rightnode.val: 
            return False
        elif not self.checkTree(rightnode.left, leftnode.right): 
            return False
        elif not self.checkTree(leftnode.left, rightnode.right): 
            return False
        else: 
            return True
        pass
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: 
            return True
        return self.checkTree(root.left, root.right)        
'''
