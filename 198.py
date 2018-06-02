class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # the state transaction between n-1 => n
        Stake = 0 
        Snot = 0
        for num in nums: 
            temp1 = Snot + num
            temp2 = max(Stake, Snot)
            Stake = temp1
            Snot = temp2
            pass
        return max(Stake, Snot)
