class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.qlen = 0

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        self.qlen = self.qlen + 1
        for index in range(self.qlen-1): 
            temp = self.queue[0]
            del self.queue[0]
            self.queue.append(temp)
            pass
        return

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        temp = self.queue[0]
        del self.queue[0]
        self.qlen = self.qlen - 1
        return temp

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self.qlen == 0: 
            return True
        else: 
            return False
        pass


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
