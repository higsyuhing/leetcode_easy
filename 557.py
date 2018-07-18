class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        res = ""
        for char in s: 
            if char != " ": 
                stack.append(char)
                pass
            else: 
                while len(stack) > 0: 
                    res += stack.pop()
                    pass
                res += " "
                pass
            pass
        while len(stack) > 0: 
            res += stack.pop()
            pass
        return res
