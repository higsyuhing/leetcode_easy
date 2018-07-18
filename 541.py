class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k <= 1: 
            return s
        stack = []
        flag = False
        res = ""
        for char in s: 
            if flag == False: 
                if len(stack) == k: 
                    while len(stack) > 0: 
                        res += stack.pop()
                        pass
                    flag = True
                    pass
                stack.append(char)
                pass
            else: 
                if len(stack) == k: 
                    res += ''.join(stack)
                    stack = []
                    flag = False
                    pass
                stack.append(char)
                pass
            pass
        if flag: 
            res += ''.join(stack)
            pass
        else: 
            while len(stack) > 0: 
                res += stack.pop()
                pass
            pass
        return res
        
