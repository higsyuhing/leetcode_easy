class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        arr = []
        for op in ops: 
            if op == "C": 
                arr.pop()
                pass
            elif op == "D": 
                if len(arr) == 0: 
                    print "Double last but none in arr: "
                    print arr
                    return 0
                temp = arr[-1]
                arr.append(2*temp)
                pass
            elif op == "+": 
                if len(arr) < 2: 
                    print "add last two but not enough in arr"
                    print arr
                    return 0
                temp1 = arr[-1]
                temp2 = arr[-2]
                arr.append(temp1 + temp2)
                pass
            else: 
                temp = int(op)
                arr.append(temp)
                pass
            pass
        return sum(arr)
        
