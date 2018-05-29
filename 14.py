class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lenMin = 0
        for index in range(len(strs)):
            temp = len(strs[index])
            if index == 0: 
                lenMin = temp
                pass
            if lenMin > temp: 
                lenMin = temp
                pass
            pass
        prefix = []
        for j in range(lenMin): 
            for index in range(len(strs)):
                temp_char = strs[index][j]
                if index == 0: 
                    prefix.append(temp_char)
                    pass
                elif temp_char != prefix[j]: 
                    del prefix[j]
                    return ''.join(prefix)
                pass
            pass
        return ''.join(prefix)
