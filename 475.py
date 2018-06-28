class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        radius = 0
        if len(heaters) == 1: 
            poshe = heaters[0]
            for posho in houses: 
                if abs(posho - poshe) > radius: 
                    radius = abs(posho - poshe)
                    pass
                pass
            return radius
        houses.sort()
        heaters.sort()
        i = 0
        j = 1
        slotshe = [heaters[0], heaters[1]]
        while i < len(houses): 
            tempx = houses[i]
            if tempx < slotshe[0]: 
                if slotshe[0] - tempx > radius: 
                    radius = slotshe[0] - tempx
                    pass
                i += 1
                pass
            elif slotshe[0] < tempx and tempx < slotshe[1]: 
                distance = min(tempx - slotshe[0], slotshe[1] - tempx)
                if distance > radius: 
                    radius = distance
                    pass
                i += 1
                pass
            elif slotshe[1] < tempx: 
                if j == len(heaters) - 1: 
                    # j is N-1 for slotshe[1], which is the last element
                    if tempx - slotshe[1] > radius: 
                        radius = houses[len(houses)-1] - slotshe[1] # directly goto the last one
                        i = len(houses)
                        pass
                    else: 
                        i += 1
                        pass
                    pass
                else: 
                    j += 1
                    slotshe[0] = slotshe[1]
                    slotshe[1] = heaters[j]
                    pass
                pass
            else: # equal to slotshe[0] or slotshe[1]
                i += 1
                pass
            pass
        return radius
        
        '''
        # this is too slow, use sorted array
        if houses == []: 
            return 0
        radius = 0
        dic = {}
        for pos in houses: 
            dic[pos] = 1
            pass
        for pos in heaters: 
            if dic.has_key(pos): 
                del dic[pos]
                pass
            pass
        while bool(dic): 
            radius += 1
            for pos in heaters: 
                pos1 = pos - radius
                if dic.has_key(pos1): 
                    del dic[pos1]
                    pass
                pos2 = pos + radius
                if dic.has_key(pos2): 
                    del dic[pos2]
                    pass
                pass
            pass
        return radius
        '''
