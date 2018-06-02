class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = {}
        for index in range(len(numbers)): 
            if hashtable.has_key(numbers[index]): 
                return [hashtable[numbers[index]], index + 1]
            else: 
                hashtable[target - numbers[index]] = index + 1
                pass
            pass
        return []
        
