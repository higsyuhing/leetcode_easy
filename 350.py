class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        for num in nums1: 
            if dic.has_key(num): 
                dic[num] += 1
                pass
            else: 
                dic[num] = 1
                pass
            pass
        res = []
        for num in nums2: 
            if dic.has_key(num): 
                res.append(num)
                dic[num] -= 1
                if dic[num] == 0: 
                    del dic[num]
                    pass
                pass
            pass
        return res
