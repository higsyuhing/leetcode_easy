class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        ## sorry, the letters are sorted... missed that
        minchar = "|"
        for char in letters: 
            if char > target and char < minchar: 
                minchar = char
                pass
            pass
        if minchar != "|": 
            return minchar
        minchar = target
        for char in letters: 
            if char < minchar: 
                minchar = char
                pass
            pass
        return minchar
