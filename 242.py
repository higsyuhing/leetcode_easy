class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if unicode char, use hash table
        array = []
        for index in range(26): 
            array.append(0)
            pass
        for char in s: 
            index = ord(char) - 97
            if index >= 0 and index < 26: 
                array[index] += 1
                pass
            pass
        for char in t: 
            index = ord(char) - 97
            if index >= 0 and index < 26: 
                array[index] -= 1
                pass
            pass
        for index in range(26): 
            if array[index] != 0: 
                return False
            pass
        return True
