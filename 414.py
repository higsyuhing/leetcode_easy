class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        for num in nums: 
            if len(arr) == 3: 
                if num > arr[0]: 
                    arr[2] = arr[1]
                    arr[1] = arr[0]
                    arr[0] = num
                    pass
                elif num < arr[0] and num > arr[1]: 
                    arr[2] = arr[1]
                    arr[1] = num
                    pass
                elif num < arr[1] and num > arr[2]: 
                    arr[2] = num
                    pass
                pass
            elif len(arr) == 2: 
                if num > arr[0]: 
                    arr.append(arr[1])
                    arr[1] = arr[0]
                    arr[0] = num
                    pass
                elif num < arr[0] and num > arr[1]: 
                    arr.append(arr[1])
                    arr[1] = num
                    pass
                elif num < arr[1]: 
                    arr.append(num)
                    pass
                pass            
            elif len(arr) == 1: 
                if num > arr[0]: 
                    arr.append(arr[0])
                    arr[0] = num
                    pass
                elif num < arr[0]: 
                    arr.append(num)
                    pass
                pass
            elif len(arr) == 0: 
                arr.append(num)
                pass
            pass
        if len(arr) < 3: 
            return arr[0]
        else: 
            return arr[2]
        pass
        
        
