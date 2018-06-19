class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for index in range(52):
            dic[index] = 0
            pass
        res = 0
        for char in s: 
            if ord(char) < 93: 
                index = ord(char) - 65
                pass
            else: 
                index = ord(char) - 97 + 26
                pass
            if dic[index] == 1: 
                res += 2
                dic[index] = 0
                pass
            else: 
                dic[index] = 1
                pass
            pass
        for index in range(52): 
            if dic[index] == 1: 
                return res+1
            pass
        return res
