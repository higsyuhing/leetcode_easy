class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # change the string to prue chars in "a-z" and "0-9"
        charlist = []
        for char in s: 
            temp = ord(char)
            if temp >= 48 and temp < 58: 
                charlist.append(temp)
                pass
            elif temp >= 65 and temp < 91: 
                charlist.append((temp + 32))
                pass
            elif temp >= 97 and temp < 123: 
                charlist.append(temp)
                pass
            else: 
                pass
            pass
        i = 0
        j = len(charlist) - 1
        while i < j: 
            if charlist[i] != charlist[j]: 
                return False
            i = i + 1
            j = j - 1
            pass
        return True
        
