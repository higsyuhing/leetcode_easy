"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ret = []
        stack = [] # already record value 
        temp = root
        while 1: 
            if temp != None: 
                if len(temp.children) > 0: 
                    ret.append(temp.val)
                    stack.append([temp, 0]) # the child index
                    temp = temp.children[0]
                    pass
                else: 
                    ret.append(temp.val)
                    temp = None # goes back
                    pass
                pass
            else: 
                if len(stack) > 0: 
                    res = stack.pop()
                    index = res[1] + 1
                    temp = res[0]
                    if len(temp.children) > index: 
                        stack.append([temp, index]) # the child index
                        temp = temp.children[index]
                        pass
                    else: 
                        temp = None # goes back
                        pass
                    pass
                else: 
                    break
                    pass
                pass
            pass
        return ret
        
        '''
        ret = []
        stack = []
        temp = root
        while 1: 
            if temp != None: 
                if len(temp.children) > 0: 
                    stack.append([temp, 0]) # the child index
                    temp = temp.children[0]
                    pass
                else: 
                    ret.append(temp.val)
                    temp = None # goes back
                    pass
                pass
            else: 
                if len(stack) > 0: 
                    res = stack.pop()
                    index = res[1] + 1
                    temp = res[0]
                    if len(temp.children) > index: 
                        stack.append([temp, index]) # the child index
                        temp = temp.children[index]
                        pass
                    else: 
                        ret.append(temp.val)
                        temp = None # goes back
                        pass
                    pass
                else: 
                    break
                    pass
                pass
            pass
        return ret
        '''
