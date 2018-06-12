class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel_arr = []
        for char in s: 
            if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or \
            char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U': 
                vowel_arr.append(char)
                pass
            pass
        res = []
        vowel_arr.reverse()
        index = 0
        for char in s: 
            if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or \
                char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U': 
                res.append(vowel_arr[index])
                index += 1
                pass
            else: 
                res.append(char)
                pass
            pass
        return ''.join(res)
