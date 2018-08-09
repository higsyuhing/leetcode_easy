class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        arr = []
        p1 = ""
        # pre-process, get rid of !?',;. and change uppercase to lowercase
        psdic = {"!":1, "?":1, "'":1, ",":1, ";":1, ".":1}
        for char in paragraph: 
            if char == " ": 
                arr.append(p1)
                p1 = ""
                continue
                pass
            if psdic.has_key(char): 
                continue
                pass
            if char >= "A" and char <= "Z": 
                p1 += str(chr(ord(char)+32))
                pass
            else: 
                p1 += str(char)
                pass
            pass
        #print p1
        # get dic
        if len(p1) > 0: 
            arr.append(p1)
            pass
        dic = {}
        for word in arr: 
            if dic.has_key(word): 
                dic[word] += 1
                pass
            else: 
                dic[word] = 1
                pass
            pass
        for word in banned: 
            if dic.has_key(word): 
                del dic[word]
                pass
            pass
        # get final
        arr1 = dic.items()
        ret = ""
        maxc = -1
        for pair in arr1: 
            if pair[1] > maxc: 
                maxc = pair[1]
                ret = pair[0]
                pass
            pass
        return ret
