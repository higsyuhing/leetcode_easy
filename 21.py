# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #'''
        res = None
        temp = None
        init_flag = 1
        temp1 = l1
        temp2 = l2
        while 1: 
            if (temp1 == None) and (temp2 == None): 
                break
                pass
            if init_flag == 1: 
                temp = ListNode(0)
                res = temp
                init_flag = 0
                pass
            else: 
                temp.next = ListNode(0)
                temp = temp.next
                pass
            if temp1 == None: 
                temp.val = temp2.val
                temp2 = temp2.next
                continue
                pass
            if temp2 == None: 
                temp.val = temp1.val
                temp1 = temp1.next
                continue
                pass
            if temp1.val > temp2.val: 
                temp.val = temp2.val
                temp2 = temp2.next
                pass
            else: 
                temp.val = temp1.val
                temp1 = temp1.next
                pass
            pass
        return res
        '''
        res = []
        i = 0
        m = len(l1)
        j = 0
        n = len(l2)
        while 1: 
            if i == m and j == n: 
                break
                pass
            if i == m: 
                res.append(l2[j])
                j = j + 1
                continue
                pass
            if j == n: 
                res.append(l1[i])
                i = i + 1
                continue
                pass
            if l1[i] > l2[j]: 
                res.append(l2[j])
                j = j + 1
                pass
            else: 
                res.append(l1[i])
                i = i + 1
                pass
            pass
        return res
        '''
            
