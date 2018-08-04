# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        num = root.val
        if root.left == None: 
            # both None
            return -1
        if root.left.val != root.right.val: 
            ## just one time solution
            ##return num^root.left.val^root.right.val
            # the ## above is incorrect
            if root.left.val == num: 
                num1 = self.findSecondMinimumValue(root.left)
                if num1 == -1: 
                    return root.right.val
                return min(num1, root.right.val)
            else: 
                num2 = self.findSecondMinimumValue(root.right)
                if num2 == -1: 
                    return root.left.val
                return min(num2, root.left.val)
            pass
        num1 = self.findSecondMinimumValue(root.left)
        num2 = self.findSecondMinimumValue(root.right)
        if num1 == -1 or num2 == -1: 
            return (-1)^num1^num2
        return min(num1, num2)
