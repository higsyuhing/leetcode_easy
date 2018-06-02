# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        fakehead = ListNode(val-1)
        fakehead.next = head
        temp = head
        res = fakehead
        parent = fakehead
        while temp != None: 
            if temp.val == val: 
                temp = temp.next
                pass
            else: 
                parent.next = temp
                parent = temp
                temp = temp.next
                pass
            pass
        parent.next = None
        temp = fakehead
        res = res.next
        del temp
        return res
