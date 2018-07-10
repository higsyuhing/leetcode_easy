class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # the dic+stack to nums is the best
        stack = []
        dic = {}
        for num in nums: 
            while stack != [] and num > stack[-1]: 
                temp = stack.pop()
                dic[temp] = num
                pass
            stack.append(num)
            pass
        while stack != []:
            temp = stack.pop()
            dic[temp] = -1
            pass
        ret = []
        for num in findNums: 
            ret.append(dic[num])
            pass
        return ret
