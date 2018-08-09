class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dic = {}
        for string in cpdomains: 
            ret = string.split()
            # len(ret) should be 2
            num = int(ret[0])
            words = ret[1].split(".")
            words.reverse()
            temp = ""
            for word in words: 
                if temp == "": 
                    temp = word
                    pass
                else: 
                    temp = word + "." + temp
                    pass
                if dic.has_key(temp): 
                    dic[temp] += num
                    pass
                else: 
                    dic[temp] = num
                    pass
                pass
            pass
        arr = dic.items()
        ret = []
        for ele in arr: 
            temp = str(ele[1]) + " " + ele[0]
            ret.append(temp)
            pass
        return ret
        
        
        
