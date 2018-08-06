class Node(object): 
    def __init__(self, x): 
        self.val = x
        self.next = None
        pass
    pass


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        pass

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        temp = self.head
        tempindex = 0
        while tempindex < index: 
            if temp == None: 
                return -1
            temp = temp.next
            tempindex += 1
            pass
        if temp == None: 
            return -1
        else: 
            return temp.val
        pass

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        temp = self.head
        self.head = Node(val)
        self.head.next = temp
        pass

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        if self.head == None: 
            self.head = Node(val)
            pass
        else: 
            temp = self.head
            while temp.next != None: 
                temp = temp.next
                pass
            temp.next = Node(val)
            pass
        pass

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index == 0: 
            self.addAtHead(val)
            return
        temp = self.head
        last = None
        tempindex = 0
        while tempindex < index: 
            if temp == None: 
                return
            last = temp
            temp = temp.next
            tempindex += 1
            pass
        last.next = Node(val)
        last.next.next = temp
        pass

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        temp = self.head
        if index == 0: 
            if temp != None: 
                self.head = temp.next
                del temp
                pass
            return
        last = None
        tempindex = 0
        while tempindex < index: 
            if temp == None: 
                return
            last = temp
            temp = temp.next
            tempindex += 1
            pass
        if temp != None: 
            last.next = temp.next
            del temp
            pass
        pass


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
