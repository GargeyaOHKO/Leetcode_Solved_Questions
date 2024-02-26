class Solution(object):
    def countBits(self, n):
        dp=[0]*(n+1)
        c=1
        for i in range(1,n+1):
            if i==(2**c):
                c+=1
            dp[i]=1+dp[i-(2**(c-1))]
        return dp    
        """
        :type n: int
        :rtype: List[int]
        """
        