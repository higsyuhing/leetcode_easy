class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        si = 0
        gi = 0
        res = 0
        while 1: 
            if si >= len(s) or gi >= len(g): 
                break
                pass
            if s[si] >= g[gi]: 
                res += 1
                si += 1
                gi += 1
                pass
            else: 
                si += 1
                pass
            pass
        return res
