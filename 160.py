# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # the solution is so smart!! 
        if headA == None or headB == None: 
            return None
        tempA = headA
        tempB = headB
        flagA = 0
        flagB = 0
        while 1: 
            if tempA == tempB: 
                return tempA
            tempA = tempA.next
            tempB = tempB.next
            if tempA == None: 
                if flagA: 
                    return None
                else: 
                    tempA = headB
                    flagA = 1
                    pass
                pass
            if tempB == None: 
                if flagB: 
                    return None
                else: 
                    tempB = headA
                    flagB = 1
                    pass
                pass
            pass
        pass
            
                
