# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def func(self, node, sum_num, target_list): 
        if node == None: 
            return 0
        n0 = 0
        for index in range(len(target_list)): 
            target_list[index] -= node.val
            if target_list[index] == 0: 
                n0 += 1
                pass
            pass
        if (sum_num - node.val) == 0: 
            n0 += 1
        target_list.append((sum_num - node.val))
        n1 = self.func(node.left, sum_num, target_list)
        n2 = self.func(node.right, sum_num, target_list)
        target_list.pop()
        for index in range(len(target_list)): 
            target_list[index] += node.val
            pass
        return n0+n1+n2
    
    def pathSum(self, root, sum_num):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root == None: 
            return 0
        return self.func(root, sum_num, [])
