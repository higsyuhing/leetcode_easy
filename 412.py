class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for index in range(n): 
            string = ''
            num = index+1
            if num%3 != 0 and num%5 != 0: 
                string = str(num)
                pass
            else: 
                if num%3 == 0: 
                    string += 'Fizz'
                    pass
                if num%5 == 0: 
                    string += 'Buzz'
                    pass
                pass
            res.append(string)
            pass
        return res
