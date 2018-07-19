"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object): 
    def nodecopy(self, qnode): 
        # create exactly same node as qnode
        if qnode == None: 
            return None
        tl = self.nodecopy(qnode.topLeft)
        tr = self.nodecopy(qnode.topRight)
        bl = self.nodecopy(qnode.bottomLeft)
        br = self.nodecopy(qnode.bottomRight)
        return Node(qnode.val, qnode.isLeaf, tl, tr, bl, br)
        
    def func(self, qnode1, qnode2): 
        # OR implementation
        if qnode1.isLeaf == True and qnode2.isLeaf == True: 
            retnode = Node(qnode1.val or qnode2.val, True, None, None, None, None)
            return retnode
        if qnode1.isLeaf == False and qnode2.isLeaf == True: 
            if qnode2.val == True: 
                return Node(True, True, None, None, None, None)
            else: 
                return self.nodecopy(qnode1)
            pass
        if qnode1.isLeaf == True and qnode2.isLeaf == False: 
            if qnode1.val == True: 
                return Node(True, True, None, None, None, None)
            else: 
                return self.nodecopy(qnode2)
            pass
        # both false
        tl = self.func(qnode1.topLeft, qnode2.topLeft)
        tr = self.func(qnode1.topRight, qnode2.topRight)
        bl = self.func(qnode1.bottomLeft, qnode2.bottomLeft)
        br = self.func(qnode1.bottomRight, qnode2.bottomRight)
        ### if tl tr bl br are all same and all leafnode, then they should be merged. 
        ### TODO: incorrect implementation
        return Node(qnode1.val or qnode2.val, False, tl, tr, bl, br)
    
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if quadTree1 == None: 
            return quadTree2
        elif quadTree2 == None: 
            return quadTree1
        # not None for both root
        return self.func(quadTree1, quadTree2)
