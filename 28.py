class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lenH = len(haystack)
        lenN = len(needle)
        if lenN == 0: 
            return 0
        if lenH < lenN: 
            return -1
        S = 0
        for char in needle: 
            S = S + ord(char)
            pass
        T = 0
        for i in range(lenH - lenN + 1): 
            if i == 0: 
                for j in range(lenN): 
                    T = T + ord(haystack[j])
                    pass
                pass
            else: 
                T = T - ord(haystack[i-1]) + ord(haystack[i + lenN - 1])
                pass
            if S == T: 
                success = 1
                for j in range(lenN): 
                    if haystack[i + j] != needle[j]: 
                        success = 0
                        break
                        pass
                    pass
                if success: 
                    return i
                pass
            pass
        return -1
