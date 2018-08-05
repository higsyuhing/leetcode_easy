class KthLargest(object):

    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        self.size = len(self.pool)
        heapq.heapify(self.pool)
        while self.size > k:
            heapq.heappop(self.pool)
            self.size -= 1

    def add(self, val):
        if self.size < self.k:
            heapq.heappush(self.pool, val)
            self.size += 1
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]
    
    '''
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        if len(nums) < k: 
            self.arr = nums + [-1000000]*(k-len(nums))
            self.arr.sort()
            pass
        else: 
            self.arr = nums[0:k]
            self.arr.sort()
            for index in range(len(nums) - k): 
                i = index + k
                self.add(nums[i])
                pass
            pass
        pass

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.arr[0] < val: 
            # update arr
            start = 0
            end = len(self.arr)
            while (end - start) > 1: 
                mid = (start + end)/2
                if self.arr[mid] < val: 
                    start = mid
                    pass
                else: 
                    end = mid
                    pass
                pass
            # [0, start] eliminstion
            for index in range(start): 
                self.arr[index] = self.arr[index + 1]
                pass
            self.arr[start] = val
            pass
        return self.arr[0]
    '''

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
