class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        state = 1000
        val = 0
        for char in s: 
            if char == 'M': 
                if state >= 1000: 
                    val = val + 1000
                    pass
                else: 
                    val = val - 200 + 1000
                    pass
                state = 1000
                pass
            elif char == 'D':
                if state >= 500:
                    val = val + 500
                    pass
                else: 
                    val = val - 200 + 500
                    pass
                state = 500
                pass
            elif char == 'C':
                if state >= 100:
                    val = val + 100
                    pass
                else: 
                    val = val - 20 + 100
                    pass
                state = 100
                pass
            elif char == 'L':
                if state >= 50:
                    val = val + 50
                    pass
                else: 
                    val = val - 20 + 50
                    pass
                state = 50
                pass
            elif char == 'X': 
                if state >= 10:
                    val = val + 10
                    pass
                else: 
                    val = val - 2 + 10
                    pass
                state = 10
                pass
            elif char == 'V': 
                if state >= 5:
                    val = val + 5
                    pass
                else: 
                    val = val - 2 + 5
                    pass
                state = 5
                pass
            elif char == 'I': 
                val = val + 1
                state = 1
                pass
            else: 
                print "Invalid char! "
                pass
            pass
        return val
        
        
