class Solution(object):
    def hammingWeight(self, n):
        c=0
        for i in range(32,-1,-1):
            if n-2**i>=0:
                c=c+1
                n=n-2**i
        return c           
        """
        :type n: int
        :rtype: int
        """
        