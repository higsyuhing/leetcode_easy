class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        stack = []
        curr = -1
        count = 1
        index = 0
        for char in chars: 
            if ord(char) != curr: 
                if count != 1: 
                    while count > 0: 
                        stack.append(count%10)
                        count = count/10
                        pass
                    while len(stack) > 0: 
                        temp = stack.pop()
                        chars[index] = str(temp)
                        index += 1
                        pass
                    pass
                chars[index] = str(char)
                index += 1
                curr = ord(char)
                count = 1
                pass
            else: 
                count += 1
                pass
            pass
        if count != 1: 
            while count > 0: 
                stack.append(count%10)
                count = count/10
                pass
            while len(stack) > 0: 
                temp = stack.pop()
                chars[index] = str(temp)
                index += 1
                pass
            pass
        return index
