class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        spaceflag = 0
        for char in s: 
            if char == ' ': 
                spaceflag = 1
                pass
            elif spaceflag == 0: 
                length = length + 1
                pass
            else: 
                length = 1
                spaceflag = 0
                pass
            pass
        return length
