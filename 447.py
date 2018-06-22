class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        dic = {}
        for i in range(len(points)): 
            pi = points[i]
            xi = pi[0]
            yi = pi[1]
            for j in range(len(points) - 1 - i): 
                pj = points[i + 1 + j]
                xj = pj[0]
                yj = pj[1]
                dis = (xj - xi)**2 + (yj - yi)**2
                if dic.has_key(dis): 
                    dic[dis].append([i, i + 1 + j])
                    pass
                else: 
                    dic[dis] = [[i, i + 1 + j]]
                    pass
                pass
            pass
        val_list = dic.values()
        count = 0
        for curr_list in val_list: 
            if len(curr_list) == 1: 
                continue
                pass
            dic.clear()
            for pair in curr_list: 
                pi = pair[0]
                pj = pair[1]
                if dic.has_key(pi): 
                    dic[pi] += 1
                    pass
                else: 
                    dic[pi] = 1
                    pass
                if dic.has_key(pj): 
                    dic[pj] += 1
                    pass
                else: 
                    dic[pj] = 1
                    pass
                pass
            point_list = dic.values()
            for num in point_list: 
                if num == 1: 
                    continue
                    pass
                else: 
                    count += num*(num-1) # A(n,2) permutation
                    pass
                pass
            pass
        return count
