class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        v = 0 # vertical: L/R
        h = 0 # horizontal: U/D
        for char in moves: 
            if char == "L": 
                v += 1
                pass
            elif char == "R": 
                v -= 1
                pass
            elif char == "U": 
                h += 1
                pass
            elif char == "D": 
                h -= 1
                pass
            else: 
                print "Error char"
                pass
            pass
        if h == 0 and v == 0: 
            return True
        else: 
            return False
        
