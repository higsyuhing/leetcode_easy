# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None: 
            return True
        stack = []
        temp = head
        while temp != None: 
            stack.append(temp.val)
            temp = temp.next
            pass
        i = 0
        j = len(stack) - 1
        while i < j: 
            if stack[i] != stack[j]: 
                return False
            i = i + 1
            j = j - 1
            pass
        return True
        

'''
class Solution(object):
    # use recursive stack as a O(n) space cost
    def func(self, node, head): 
        if node == None: 
            return [True, head]
        else: 
            res = self.func(node.next, head)
            if res[0] == False: 
                return res
            if node.val == res[1].val: 
                return [True, res[1].next]
            else: 
                return [False, res[1]]
            pass
        pass
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        res = self.func(head, head)
        return res[0]
'''
