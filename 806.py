class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lmax = 100
        lnum = 0
        lpos = 0
        for char in S: 
            temp = widths[ord(char)-97]
            if (lpos + temp) <= lmax: 
                lpos += temp
                pass
            else: 
                lnum += 1
                lpos = temp
                pass
            pass
        return [lnum+1, lpos]
