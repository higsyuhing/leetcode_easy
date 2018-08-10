class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        index = 1
        res = []
        vowel = {"a":1, "A":1, "e":1, "E":1, "i":1, "I":1, "o":1, "O":1, "u":1, "U":1}
        arr = S.split()
        for word in arr: 
            head = word[0]
            if len(word) == 1 or vowel.has_key(head): 
                temp = word + "ma"
                pass
            else: 
                tail = word[1:]
                temp = tail + head + "ma"
                pass
            for i in range(index): 
                temp += "a"
                pass
            res.append(temp)
            index += 1
            pass
        return " ".join(res)
        
        
        
        
            
