class Solution(object):
    def wordPattern(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dic = {}
        dic_rev = {}
        array = []
        pt_index = 0
        str_index = 0
        while 1: 
            # no pattern remains
            if pt_index == len(pattern): 
                '''
                while str_index < len(string): 
                    if string[str_index] == ' ': 
                        str_index += 1
                        pass
                    else: 
                        break
                        pass
                    pass
                '''
                if str_index < len(string): 
                    return False # no pattern but contain non-empty string
                else: 
                    break
                pass
            # pattern remains, pick one
            pt = pattern[pt_index]
            pt_index += 1
            
            # exclude ' 's
            temp_arr = []
            while str_index < len(string): 
                if string[str_index] == ' ': 
                    str_index += 1
                    pass
                else: 
                    break
                    pass
                pass
            # no string remains
            if str_index == len(string): 
                return False # contain pattern but no matched string
            # string remains, pick one
            while str_index < len(string): 
                if string[str_index] != ' ': 
                    temp_arr.append(string[str_index])
                    str_index += 1
                    pass
                else: 
                    break
                    pass
                pass
            temp_str = "".join(temp_arr)
            array.append(temp_str)
            
            # compare
            if dic.has_key(pt): 
                if dic[pt] != temp_str: 
                    return False
                pass
            else: 
                dic[pt] = temp_str
                pass
            if dic_rev.has_key(temp_str): 
                if dic_rev[temp_str] != pt: 
                    return False
                pass
            else: 
                dic_rev[temp_str] = pt
                pass
            pass
        return True
            
            
