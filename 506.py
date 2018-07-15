def takeSecond(elem):
    return elem[1]

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        arr = []
        index = 1
        for num in nums: 
            arr.append([num, index])
            index += 1
            pass
        arr.sort(reverse=True)
        count = 0
        for index in range(len(arr)): 
            count += 1
            if count > 3: 
                arr[index][0] = str(count)
                continue
                pass
            if count == 1: 
                arr[index][0] = "Gold Medal"
                pass
            elif count == 2: 
                arr[index][0] = "Silver Medal"
                pass
            else: 
                arr[index][0] = "Bronze Medal"
                pass
            pass
        arr.sort(key=takeSecond)
        ret = []
        for ele in arr: 
            ret.append(ele[0])
            pass
        return ret
