class Solution(object):
    def hammingWeight(self, n):
        c=0
        while n>0:
            if 1&n==1:
                c=c+1
            n=n>>1
        return c           
        """
        :type n: int
        :rtype: int
        """
        