# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # method 1: traverse all node with a dic, 
        # I don't think it's good since it doesn't use BST
        # but tree [2, 1, null, null, 2] is possible to make it hard
        # it beats 97.24% ?!
        # CSDN has the better middle-val-traverse mathod, which is better
        dic = {}
        temp = root
        stack = []
        while 1: 
            if temp != None: 
                stack.append(temp)
                temp = temp.left
                pass
            else: 
                if stack != []: 
                    temp = stack.pop()
                    if dic.has_key(temp.val): 
                        dic[temp.val] += 1
                        pass
                    else: 
                        dic[temp.val] = 1
                        pass
                    temp = temp.right
                    pass
                else: 
                    break
                    pass
                pass
            pass
        ret = []
        arr = dic.items()
        count = 0
        for pair in arr: 
            if pair[1] > count: 
                count = pair[1]
                pass
            pass
        for pair in arr: 
            if pair[1] == count: 
                ret.append(pair[0])
                pass
            pass
        return ret
