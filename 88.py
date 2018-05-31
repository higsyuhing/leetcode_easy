class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        while (i >= 0) and (j >= 0): 
            if nums1[i] > nums2[j]: 
                nums1[k] = nums1[i]
                i = i - 1
                k = k - 1
                pass
            else: 
                nums1[k] = nums2[j]
                j = j - 1
                k = k - 1
                pass
            pass
        while (j >= 0): 
            nums1[k] = nums2[j]
            j = j - 1
            k = k - 1
            pass
        return

'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        array = []
        while 1: 
            if i == m: 
                array = array + nums2[j:n]
                break
                pass
            elif j == n: 
                array = array + nums1[i:m]
                break
                pass
            elif nums2[j] <= nums1[i]: 
                array = array + [nums2[j]]
                j = j + 1
                pass
            else: 
                array = array + [nums1[i]]
                i = i + 1
                pass
            pass
        index = 0
        for num in array: 
            nums1[index] = num
            index = index + 1
        return
'''             
            
