class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = []
        length = len(S)
        count = 0
        for index in range(length):
            char = S[length - 1 - index]
            if char == '-': 
                continue
                pass
            if ord(char) >= 97: 
                s.append(chr(ord(char) - 97 + 65))
                pass
            else: 
                s.append(char)
                pass
            count += 1
            if count == K: 
                s.append('-')
                count = 0
                pass
            pass
        if len(s) > 0 and s[len(s)-1] == '-': 
            s.pop()
            pass
        s.reverse()
        #print s
        return "".join(s)
        '''
        for char in S: 
            if char == '-': 
                continue
                pass
            if ord(char) >= 97: 
                s.append(chr(ord(char) - 97 + 65))
                pass
            else: 
                s.append(char)
                pass
            pass
        #print s
        length = len(s) - K
        while length > 0: 
            s = s[0:length] + ['-'] + s[length:]
            length -= K
            pass
        #print s
        return "".join(s)
        '''
