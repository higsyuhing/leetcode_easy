class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        Aflag = False
        preLcount = 0
        for char in s: 
            #print char, Aflag, preLcount
            if char == "A": 
                if Aflag: 
                    return False
                Aflag = True
                preLcount = 0
                pass
            elif char == "L": 
                if preLcount > 1: 
                    return False
                else: 
                    preLcount += 1
                    pass
                pass
            else: 
                preLcount = 0
                pass
            pass
        return True
