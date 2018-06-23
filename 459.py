class Solution(object):
    def func(self, pattern, s): 
        si = len(pattern)
        pi = 0
        while si < len(s): 
            if pattern[pi] != s[si]: 
                return False
            si += 1
            pi += 1
            if pi == len(pattern): 
                pi = 0
                pass
            pass
        return True
    
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # lexer: S <= sS | e
        pattern = ''
        upbound = int(len(s)/2)
        for i in range(upbound): 
            pattern += s[i]
            if len(s)%len(pattern) != 0: 
                continue
                pass
            if self.func(pattern, s): 
                print pattern
                return True
            pass
        return False
