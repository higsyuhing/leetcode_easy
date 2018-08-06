class orderqueue(object): 
    def __init__(self): 
        self.arr = []
        self.len = 0
        pass
    
    def insert(self, key, value): 
        start = -1
        end = self.len
        while (end - start) > 1: 
            mid = (start + end)/2
            if self.arr[mid][0] < key: 
                start = mid
                pass
            elif self.arr[mid][0] > key: 
                end = mid
                pass
            else: 
                # find duplicate, update value
                self.arr[mid][1] = value
                return
            pass
        # insert start+1
        self.arr.insert(start+1, [key, value])
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
            if self.arr[mid][0] < key: 
                start = mid
                pass
            elif self.arr[mid][0] > key: 
                end = mid
                pass
            else: 
                #print "find: pos: ", mid
                return mid
            pass
        #print "find: pos: -1"
        return -1
    
    def access(self, key): 
        index = self.find(key)
        if index == -1: 
            return -1
        else: 
            return self.arr[index][1]
        pass

class MyHashMap(object):

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

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        index = key%1000
        self.hash[index].insert(key, value)
        pass

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key%1000
        return self.hash[index].access(key)

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = key%1000
        self.hash[index].delete(key)
        pass


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
