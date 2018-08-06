class orderqueue(object): 
    def __init__(self): 
        self.arr = []
        self.len = 0
        pass
    
    def insert(self, key): 
        start = -1
        end = self.len
        while (end - start) > 1: 
            mid = (start + end)/2
            if self.arr[mid] < key: 
                start = mid
                pass
            elif self.arr[mid] > key: 
                end = mid
                pass
            else: 
                # find duplicate
                return
            pass
        # insert start+1
        self.arr.insert(start+1, key)
        self.len += 1
        #print "insert: pos: ", (start+1), ", key: ", key
        pass
    
    def delete(self, key): 
        index = self.find(key)
        #print "delete: pos: ", index
        if index >= 0: 
            del self.arr[index]
            self.len -= 1
            pass
        pass
    
    def find(self, key): 
        start = -1
        end = self.len
        while (end - start) > 1: 
            mid = (start + end)/2
            if self.arr[mid] < key: 
                start = mid
                pass
            elif self.arr[mid] > key: 
                end = mid
                pass
            else: 
                #print "find: pos: ", mid
                return mid
            pass
        #print "find: pos: -1"
        return -1

class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # do it by 1000*1000, [0, 1000000]
        self.hash = []
        for i in range(1000): 
            temp = orderqueue()
            self.hash.append(temp)
            pass
        pass

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        index = key%1000
        self.hash[index].insert(key)
        pass

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        index = key%1000
        self.hash[index].delete(key)
        pass

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        index = key%1000
        ret = self.hash[index].find(key)
        return (ret > -1)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
