class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        # -1: init, 0-n, one-time pos, -2 invalid
        for i in range(26): 
            dic[i] = -1
            pass
        for i in range(len(s)):
            char = s[i]
            index = ord(char) - 97
            res = dic[index]
            if res == -2: 
                continue
                pass
            if res == -1: 
                dic[index] = i
                pass
            else: 
                dic[index] = -2
                pass
            pass
        minindex = -1
        for i in range(26): 
            if dic[i] >= 0: 
                if minindex == -1 or minindex > dic[i]: 
                    minindex = dic[i]
                    pass
                pass
            pass
        return minindex
        
