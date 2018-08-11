class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        charge = [0, 0] # number of 5 and 10
        for num in bills: 
            if num == 5: 
                charge[0] += 1
                pass
            elif num == 10: 
                if charge[0] == 0: 
                    return False
                charge[0] -= 1
                charge[1] += 1
                pass
            else: 
                if charge[0] > 0 and charge[1] > 0: 
                    charge[1] -= 1
                    charge[0] -= 1
                    pass
                elif charge[0] > 3: 
                    charge[0] -= 3
                    pass
                else: 
                    return False
                pass
            pass
        return True
    
