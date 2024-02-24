class Solution(object):
    def hammingWeight(self, n):
        c=0
        while n>0:
            n=n&(n-1)
            c=c+1
        return c           
        """
        :type n: int
        :rtype: int
        """
        