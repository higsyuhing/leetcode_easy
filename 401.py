class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num > 8 or num < 0: 
            return []
        # hour = [] # 1 2 4 8
        # minute = [] # 1 2 4 8 16 32
        hdic = {}
        mdic = {}
        for index in range(12): 
            temp = index
            hour = []
            while temp > 0: 
                hour.append(temp%2)
                temp = temp/2
                pass
            key = sum(hour)
            if hdic.has_key(key): 
                hdic[key].append(str(index))
                pass
            else: 
                hdic[key] = [str(index)]
                pass
            pass
        #print hdic
        numh = 4
        for index in range(60): 
            temp = index
            minute = []
            while temp > 0: 
                minute.append(temp%2)
                temp = temp/2
                pass
            key = sum(minute)
            if index < 10: 
                string = '0' + str(index)
                pass
            else: 
                string = str(index)
                pass
            if mdic.has_key(key): 
                mdic[key].append(string)
                pass
            else: 
                mdic[key] = [string]
                pass
            pass
        #print mdic
        numm = 6
        
        res = []
        for i in range(numh): 
            for j in range(numm): 
                if i + j == num: 
                    for indi in range(len(hdic[i])): 
                        for indj in range(len(mdic[j])): 
                            res.append((hdic[i][indi] + ':' + mdic[j][indj]))
                            pass
                        pass
                    pass
                pass
            pass
        return res
