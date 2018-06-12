class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        for num in nums1: 
            if dic.has_key(num): 
                pass
            else: 
                dic[num] = True
                pass
            pass
        res = []
        for num in nums2: 
            if dic.has_key(num): 
                res.append(num)
                del dic[num]
                pass
            pass
        return res
