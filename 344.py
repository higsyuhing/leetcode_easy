class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        length = len(s)
        for index in range(length): 
            res.append(s[length - 1 - index])
            pass
        return ''.join(res)
