class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # contain [element, ptr to Min]
        self.stack = []
        self.slen = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.slen == 0: 
            self.stack.append([x, 0])
            self.slen = self.slen + 1
            pass
        else: 
            currMinIndex = self.stack[self.slen-1][1]
            if self.stack[currMinIndex][0] > x: 
                self.stack.append([x, self.slen])
                self.slen = self.slen + 1
                pass
            else: 
                self.stack.append([x, currMinIndex])
                self.slen = self.slen + 1
                pass
            pass
        return

    def pop(self):
        """
        :rtype: void
        """
        if self.slen != 0: 
            res = self.stack.pop()
            self.slen = self.slen - 1
            pass
        return

    def top(self):
        """
        :rtype: int
        """
        return self.stack[self.slen - 1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[self.stack[self.slen - 1][1]][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
