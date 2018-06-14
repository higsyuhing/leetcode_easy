class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = {}
        for i in range(26): 
            dic[i] = 0
            pass
        for char in ransomNote: 
            index = ord(char) - 97
            dic[index] -= 1
            pass
        for char in magazine: 
            index = ord(char) - 97
            dic[index] += 1
            pass
        for i in range(26): 
            if dic[i] < 0: 
                return False
            pass
        return True
