class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)

        self.total=0
        def dfs(i):
            if i==n:
                return 1   
            if i>n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            dp[i]=dfs(i+1)+dfs(i+2)
            #print(dp)
            return dp[i]
        return dfs(0)
        print(dp)
        #print(dp)
