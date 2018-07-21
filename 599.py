class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic = {}
        for index in range(len(list1)): 
            name = list1[index]
            dic[name] = [index, -1]
            pass
        for index in range(len(list2)): 
            name = list2[index]
            if dic.has_key(name): 
                dic[name][1] = index
                pass
            pass
        arr = dic.items()
        res = []
        currsum = -1
        for ele in arr: 
            if ele[1][1] != -1: # in both list
                if currsum == -1: 
                    currsum = ele[1][0] + ele[1][1]
                    res.append(ele[0])
                    pass
                else: 
                    tempsum = ele[1][0] + ele[1][1]
                    if tempsum < currsum: 
                        res = []
                        currsum = tempsum
                        res.append(ele[0])
                        pass
                    elif tempsum == currsum: 
                        res.append(ele[0])
                        pass
                    pass
                pass
            pass
        return res
    
