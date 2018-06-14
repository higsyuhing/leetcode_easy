class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        temp = 0
        for char in s: 
            temp = temp ^ ord(char)
            pass
        for char in t: 
            temp = temp ^ ord(char)
            pass
        return chr(temp)
