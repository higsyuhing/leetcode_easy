class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for index in range(len(digits)): 
            curr = len(digits) - 1 - index
            if carry == 1:
                if digits[curr] == 9: 
                    digits[curr] = 0
                    pass
                else: 
                    digits[curr] = digits[curr] + 1
                    carry = 0
                    pass
                pass
            else: 
                break
                pass
            pass
        if carry == 1: 
            digits = [1] + digits
            pass
        return digits
