class alphaTree(object): 
    def __init__(self): 
        self.alpha = []
        for i in range(26): 
            self.alpha.append(None)
            pass
        pass
    
    def add(self, word): 
        if len(word) == 0: 
            #print "add: word: ", word, " is empty string"
            return -1
        temp = self
        for i in range(len(word)-1): 
            index = ord(word[i]) - 97 # a => 0
            if temp.alpha[index] == None: 
                #print "add: word: ", word, " at index: ", index, " is undef in alphatree"
                return -1
            temp = temp.alpha[index]
            pass
        index = ord(word[-1]) - 97
        if temp.alpha[index] != None: 
            #print "add: word: ", word, " at index: ", index, " has def"
            return -1
        temp.alpha[index] = alphaTree()
        return 0        
    
    '''
    def treedepth(self): 
        currdepth = 0
        for i in range(26): 
            if self.alpha[i] != None: 
                currdepth = max(currdepth, self.alpha[i].treedepth())
                pass
            pass
        # -1 at highest level
        return currdepth + 1
    '''
    
    def longestword(self): 
        curr = [0, ""]
        for i in range(26): 
            if self.alpha[i] != None: 
                ret = self.alpha[i].longestword()
                ret[0] += 1
                ret[1] = str(chr(i+97)) + ret[1]
                if ret[0] > curr[0]: 
                    curr = ret
                    pass
                pass
            pass
        return curr

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # this is a sorting problem... 
        words.sort()
        #print words
        atree = alphaTree()
        for word in words: 
            atree.add(word)
            pass
        ret = atree.longestword()
        return ret[1]
        
        
        
                
