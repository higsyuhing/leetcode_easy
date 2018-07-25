class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = nums[0]
        arrmax = [-1001, -1001, -1001]
        arrmin = [1001, 1001]
        for num in nums: 
            if num <= arrmax[0]: 
                pass
            elif num <= arrmax[1]: 
                arrmax[0] = num
                pass
            elif num <= arrmax[2]: 
                arrmax[0] = arrmax[1]
                arrmax[1] = num
                pass
            else: 
                arrmax[0] = arrmax[1]
                arrmax[1] = arrmax[2]
                arrmax[2] = num
                pass
            
            if num >= arrmin[0]: 
                pass
            elif num >= arrmin[1]: 
                arrmin[0] = num
                pass
            else: 
                arrmin[0] = arrmin[1]
                arrmin[1] = num
                pass
            pass
        return max(arrmax[0]*arrmax[1]*arrmax[2], arrmin[0]*arrmin[1]*arrmax[2])
        
        
        
        
        '''
        # this is a stupid idea. see sol 3
        arrpos = [-1, -1, -1] # pos max numbers
        arrneg0 = [1, 1, 1] # neg close to 0
        arrneg = [1, 1, 1] # neg max numbers
        for num in nums: 
            if num > 0: 
                if num < arrpos[0]: 
                    pass
                elif num < arrpos[1]: 
                    arrpos[0] = num
                    pass
                elif num < arrpos[2]: 
                    arrpos[0] = arrpos[1]
                    arrpos[1] = num
                    pass
                else: 
                    arrpos[0] = arrpos[1]
                    arrpos[1] = arrpos[2]
                    arrpos[2] = num
                    pass
                pass
            else: 
                if num < arrneg0[0]: 
                    pass
                elif num < arrneg0[1]: 
                    arrneg0[0] = num
                    pass
                elif num < arrneg0[2]: 
                    arrneg0[0] = arrneg0[1]
                    arrneg0[1] = num
                    pass
                else: 
                    arrneg0[0] = arrneg0[1]
                    arrneg0[1] = arrneg0[2]
                    arrneg0[2] = num
                    pass
                
                if num > arrneg[0]: 
                    pass
                elif num > arrneg[1]: 
                    arrneg[0] = num
                    pass
                elif num > arrneg[2]: 
                    arrneg[0] = arrneg[1]
                    arrneg[1] = num
                    pass
                else: 
                    arrneg[0] = arrneg[1]
                    arrneg[1] = arrneg[2]
                    arrneg[2] = num
                    pass
                pass
            pass
        if arrpos[2] > -1: # exist pos number
            if arrneg[2] < 1: #exist neg number
                
                
                pass
            else: 
                if arrpos[0] == -1: 
                    print "Error! unknown case: "
                    print "arrpos: ", arrpos
                    print "arrneg0: ", arrneg0
                    print "arrneg: ", arrneg
                    return 0
                res = arrpos[2]*arrpos[1]*arrpos[0]
                return res
            pass
        else: 
            
            
            pass
        
        return 0
        '''
