# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # hash function is not good. 
        # but two pointers will cost extra K cycle
        if head == None or head.next == None: 
            return False
        slow = head
        fast = head.next
        while 1: 
            if fast == None or fast.next == None: 
                return False
            if slow == fast: 
                return True
            slow = slow.next
            fast = fast.next.next
            pass
        pass
            
        
