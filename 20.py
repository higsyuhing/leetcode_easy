class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        length = 0
        for char in s: 
            if char == '(': 
                stack.append(1)
                length = length + 1
                pass
            elif char == ')':
                if length == 0: 
                    return False
                if stack[length-1] != 1: 
                    return False
                del stack[length-1]
                length = length - 1
                pass
            elif char == '[':
                stack.append(2)
                length = length + 1
                pass
            elif char == ']':
                if length == 0: 
                    return False
                if stack[length-1] != 2: 
                    return False
                del stack[length-1]
                length = length - 1
                pass
            elif char == '{':
                stack.append(3)
                length = length + 1
                pass
            elif char == '}':
                if length == 0: 
                    return False
                if stack[length-1] != 3: 
                    return False
                del stack[length-1]
                length = length - 1
                pass
            else: 
                print "Invalid char! "
                pass
            pass
        if length != 0: 
            return False
        return True
    
