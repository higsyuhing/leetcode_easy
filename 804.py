class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        translate = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        twords = []
        for word in words: 
            temp = ""
            for char in word: 
                index = ord(char) - 97
                temp += translate[index]
                pass
            twords.append(temp)
            pass
        twords.sort()
        ret = 0
        last = ""
        for word in twords: 
            if word != last: 
                ret += 1
                last = word
                pass
            pass
        return ret
