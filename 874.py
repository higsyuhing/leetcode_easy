class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        # prepare
        obdic = {}
        for ob in obstacles: 
            r = ob[0]
            c = ob[1]
            if obdic.has_key(r): 
                obdic[r][c] = 1
                pass
            else: 
                obdic[r] = {c:1}
                pass
            pass
        face = {0:[0, 1], 1:[-1, 0], 2:[0, -1], 3:[1, 0]}
        
        currpos = [0, 0]
        currface = 0 # N-0, W-1, S-2, E-3
        ret = 0
        for num in commands: 
            if num == -2: 
                currface = (currface + 1)%4
                pass
            elif num == -1: 
                currface = (currface - 1 + 4)%4
                pass
            else: 
                move = face[currface]
                for i in range(num): 
                    temppos = [currpos[0] + move[0], currpos[1] + move[1]]
                    if obdic.has_key(temppos[0]): 
                        if obdic[temppos[0]].has_key(temppos[1]): 
                            break
                            pass
                        pass
                    currpos = temppos
                    pass
                pass
            dis = currpos[0]**2 + currpos[1]**2
            if dis > ret: 
                ret = dis
                pass
            pass
        return ret
        
        
        
        
        
        
        
