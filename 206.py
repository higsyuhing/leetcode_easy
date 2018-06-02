# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: 
            return head
        temp = head.next
        parent = head
        parent.next = None
        while temp != None: 
            curr = temp
            temp = temp.next
            curr.next = parent
            parent = curr
            pass
        return parent
