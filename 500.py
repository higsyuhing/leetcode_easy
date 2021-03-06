class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        dic = {
            'Q': 1, 'q': 1, 'W': 1, 'w': 1, 'E': 1, 'e': 1, 'R': 1, 'r': 1, 'T': 1, 't': 1, 'Y': 1, 'y': 1, 'U': 1, 'u': 1, 'I': 1, 'i': 1, 'O': 1, 'o': 1, 'P': 1, 'p': 1, 
            'A': 2, 'a': 2, 'S': 2, 's': 2, 'D': 2, 'd': 2, 'F': 2, 'f': 2, 'G': 2, 'g': 2, 'H': 2, 'h': 2, 'J': 2, 'j': 2, 'K': 2, 'k': 2, 'L': 2, 'l': 2, 
            'Z': 3, 'z': 3, 'X': 3, 'x': 3, 'C': 3, 'c': 3, 'V': 3, 'v': 3, 'B': 3, 'b': 3, 'N': 3, 'n': 3, 'M': 3, 'm': 3
        }
        ret = []
        for word in words: 
            flag = True
            row = 0
            for char in word: 
                if row == 0: 
                    row = dic[char]
                    pass
                elif row != dic[char]: 
                    flag = False
                    break
                    pass
                pass
            if flag: 
                ret.append(word)
                pass
            pass
        return ret
        
