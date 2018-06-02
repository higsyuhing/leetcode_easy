class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.slen = 0
        self.curr = 1 # push stack, 2 for pop stack

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if self.curr == 1: 
            self.stack1.append(x)
            self.slen = self.slen + 1
            pass
        else: 
            for index in range(self.slen): 
                self.stack1.append(self.stack2.pop())
                pass
            self.stack1.append(x)
            self.slen = self.slen + 1
            self.curr = 1
            pass
        return

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.slen == 0: 
            print "Error! "
            return 0
        if self.curr == 1: 
            for index in range(self.slen-1): 
                self.stack2.append(self.stack1.pop())
                pass
            self.slen = self.slen - 1
            self.curr = 2
            return self.stack1.pop()
        else: 
            self.slen = self.slen - 1
            return self.stack2.pop()
        pass

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.slen == 0: 
            print "Error! "
            return 0
        if self.curr == 1: 
            for index in range(self.slen): 
                self.stack2.append(self.stack1.pop())
                pass
            self.curr = 2
            return self.stack2[self.slen-1]
        else: 
            return self.stack2[self.slen-1]
        pass

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.slen == 0: 
            return True
        else: 
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
