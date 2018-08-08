class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        dic = {0:0, 1:1, 2:5, 3:-1, 4:-1, 5:2, 6:9, 7:-1, 8:8, 9:6}
        count = 0
        for i in range(N): 
            num = i + 1
            temp = num
            arr = []
            flag = True
            while temp > 0: 
                curr = temp%10
                curr = dic[curr]
                if curr == -1: 
                    flag = False
                    break
                    pass
                arr.append(curr)
                temp = temp/10
                pass
            if flag == False: 
                continue
                pass
            arr.reverse()
            temp = 0
            for j in arr: 
                temp = temp*10 + j
                pass
            if temp != num: 
                #print num
                count += 1
                pass
            pass
        return count
            
