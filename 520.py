class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cflag = True
        for char in word: 
            if ord(char) > 94 and cflag == True: 
                cflag = False
                pass
            if ord(char) < 94 and cflag == False: 
                return False
            pass
        if len(word) > 2 and cflag == False and ord(word[1]) < 94: 
            return False
        else: 
            return True
        pass
