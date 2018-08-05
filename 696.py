class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = "e"
        lastc = 0
        curr = "e" # empty
        currc = 0
        count = 0
        for char in s: 
            if curr == "e": 
                curr = char
                currc = 1
                pass
            else: 
                if curr == char: 
                    currc += 1
                    pass
                else: 
                    if last == "e": 
                        last = curr
                        lastc = currc
                        curr = char
                        currc = 1
                        pass
                    else: 
                        count += min(lastc, currc)
                        last = curr
                        lastc = currc
                        curr = char
                        currc = 1
                        pass
                    pass
                pass
            pass
        count += min(lastc, currc)
        return count
                        
                        
                        
