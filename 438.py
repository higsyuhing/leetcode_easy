class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s): 
            return []
        dic = {}
        for index in range(26): 
            dic[index] = 0
            pass
        for char in p: 
            dic[ord(char)-97] += 1
            pass
        lengthp = len(p)
        res = []
        for index in range(len(s)-lengthp+1): 
            if index == 0: 
                # first run
                for i in range(lengthp): 
                    dic[ord(s[i])-97] -= 1
                    pass
                pass
            else: 
                dic[ord(s[index-1])-97] += 1
                dic[ord(s[index-1+lengthp])-97] -= 1
                pass
            flag = 1
            for i in range(26): 
                if dic[i] != 0: 
                    flag = 0
                    break
                    pass
                pass
            if flag: 
                res.append(index)
                pass
            pass
        return res
        
