# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        arr = [] # ele: [sum, num of node] 
        numnodearr = []
        level = 0
        temp = root
        stack = []
        while 1: 
            #print arr, level
            if temp != None: 
                if level == len(arr): 
                    arr.append(float(temp.val))
                    numnodearr.append(float(1))
                    pass
                else: 
                    arr[level] += temp.val
                    numnodearr[level] += 1
                    pass
                level += 1
                stack.append([temp, 0])
                temp = temp.left
                pass
            else: 
                if len(stack) > 0: 
                    if stack[-1][1] == 1: 
                        stack.pop()
                        level -= 1
                        pass
                    else: 
                        temp = stack[-1][0].right
                        stack[-1][1] = 1
                        pass
                    pass
                else: 
                    break
                    pass
                pass
            pass
        for index in range(len(arr)): 
            arr[index] = arr[index]/numnodearr[index]
            pass
        return arr
        
        
