class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        index = 0
        flag = True
        while index < len(bits): 
            if bits[index] == 0: 
                index += 1
                flag = True
                pass
            else: 
                index += 2
                flag = False
                pass
            pass
        return flag
