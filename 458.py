class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        # this reminds me the fault tolerance in distributed sys
        # there is an algorithm using sqrt of n to determine the error node in DS
        # let's see... 
        # ...
        # use the cross dicision: dim * cut * stage
        # since if pig is live, the other half is dead for sure, then cut = 2
        # ... 
        # check the sol, OK...
        stage = int(minutesToTest/minutesToDie)
        N_inStage = stage + 1
        return int(math.ceil(math.log(buckets, N_inStage)))
