class Solution(object):
    def toLowerCase(self, string):
        """
        :type str: str
        :rtype: str
        """
        arr = ""
        for char in string: 
            if ord(char) >= 65 and ord(char) < 91: 
                arr += chr(ord(char) + 32)
                pass
            else: 
                arr += char
                pass
            pass
        return arr
        
