class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rownum = len(grid)
        colnum = len(grid[0])
        res = 0
        col_status = 0  # one row
        row_status = [] # all column
        for index in range(colnum): 
            row_status.append(0)
            pass
        for row in grid: 
            col_status = 0
            for index in range(colnum): 
                ele = row[index]
                if ele ^ col_status: 
                    res += 1
                    col_status = ele
                    pass
                if ele ^ row_status[index]: 
                    res += 1
                    row_status[index] = ele
                    pass
                pass
            if col_status == 1: 
                res += 1
                pass
            pass
        for index in range(colnum): 
            if row_status[index] == 1: 
                res += 1
                pass
            pass
        return res
                
