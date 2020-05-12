class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for c in S: 
            if len(stack) > 0: 
                if stack[-1] == c: 
                    del stack[-1]
                    continue
                    pass
                pass
            stack.append(c)
            pass
        return "".join(stack)
        
        
