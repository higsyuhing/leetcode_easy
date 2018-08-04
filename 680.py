class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        flag = True
        index = 0
        while 1: 
            if index >= (length - 1 - index): 
                break
                pass
            if s[index] != s[length - 1 - index]: 
                flag = False
                break
                pass
            index += 1
            pass
        if flag: 
            return True
        temp = index
        # 1 part, skip the upper one
        flag = True
        while 1: 
            if index >= (length - 2 - index): 
                break
                pass
            if s[index] != s[length - 2 - index]: 
                flag = False
                break
                pass
            index += 1
            pass
        if flag: 
            return True
        # 2 part, skip the lower one
        index = temp
        flag = True
        while 1: 
            if (index + 1) >= (length - 1 - index): 
                break
                pass
            if s[index + 1] != s[length - 1 - index]: 
                flag = False
                break
                pass
            index += 1
            pass
        if flag: 
            return True
        return False
        
