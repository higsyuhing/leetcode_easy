# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: 
            return head
        temp1 = head
        temp2 = head.next
        while temp2 != None: 
            if temp1.val == temp2.val: 
                temp1.next = temp2.next
                del temp2
                temp2 = temp1.next
                pass
            else: 
                temp1 = temp2
                temp2 = temp2.next
                pass
            pass
        return head
