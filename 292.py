class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 4 is the key number
        if n%4 == 0: 
            return False
        else: 
            return True
        pass
