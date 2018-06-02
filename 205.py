class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): 
            return False
        table12 = {}
        table21 = {}
        for index in range(len(s)): 
            char1 = s[index]
            char2 = t[index]
            if table12.has_key(char1): 
                if table12[char1] != char2: 
                    return False
                pass
            else: 
                table12[char1] = char2
                pass
            if table21.has_key(char2): 
                if table21[char2] != char1: 
                    return False
                pass
            else: 
                table21[char2] = char1
                pass
            pass
        return True
