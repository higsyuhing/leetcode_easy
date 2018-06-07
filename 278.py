# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0 # good version pos (1 might be bad)
        end = n # bad version pos
        while (end - start > 1): 
            test = (start + end)/2
            if isBadVersion(test): 
                end = test
                pass
            else: 
                start = test
                pass
            pass
        return end
