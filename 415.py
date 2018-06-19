class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        list1 = []
        list2 = []
        res = []
        for char in num1: 
            list1.append(ord(char)-48)
            pass
        for char in num2: 
            list2.append(ord(char)-48)
            pass
        list1.reverse()
        list2.reverse()
        carry = 0
        index = 0
        while 1: 
            if index < len(list1): 
                n1 = list1[index]
                pass
            else: 
                n1 = -1
                carry += 1
                pass
            if index < len(list2): 
                n2 = list2[index]
                pass
            else: 
                n2 = -1
                carry += 1
                pass
            s = n1 + n2 + carry
            #print res, s, carry
            if s == 0 and carry == 2: 
                break
            res.append(s%10)
            carry = s/10
            index += 1
            pass
        res.reverse()
        return ''.join(str(e) for e in res)
