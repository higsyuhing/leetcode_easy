class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        numa = 0
        for char in a: 
            numa = numa << 1
            if char == '1': 
                numa = numa + 1
                pass
            pass
        numb = 0
        for char in b: 
            numb = numb << 1
            if char == '1': 
                numb = numb + 1
                pass
            pass
        numc = numa + numb
        if numc == 0: 
            return '0'
        numclist = []
        while numc > 0: 
            numclist = [str(numc%2)] + numclist
            numc = numc >> 1
            pass
        return ''.join(numclist)
