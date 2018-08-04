"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, idn):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        dic = {}
        index = 0
        for worker in employees: 
            dic[worker.id] = index
            index += 1
            pass
        stack = []
        stack.append(idn)
        count = 0
        while len(stack) > 0: 
            index = dic[stack.pop()]
            worker = employees[index]
            count += worker.importance
            stack += worker.subordinates
            pass
        return count
        
        
        
        
        
        
        
        
        
        
