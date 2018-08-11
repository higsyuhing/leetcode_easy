# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def func(self, node, index): 
        # will return: [the node (or empty), the target index]
        if node == None: 
            # the end of list, return the target index
            return [None, index/2]
        # continue, if not the end
        ret = self.func(node.next, index + 1)
        if index == ret[1]: 
            return [node, index]
        else: 
            return ret
        pass
    
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ret = self.func(head, 0)
        return ret[0]
        
