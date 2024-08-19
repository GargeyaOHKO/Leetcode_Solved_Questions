class Solution:
    def minSteps(self, n: int) -> int:
        if n==2:
            return 2
        dp={}
        def dfs(curr,i,c):
            if curr>n:
                return float('inf') 
            if curr==n:
                return c
            if (curr,i) in dp:
                return dp[(curr,i)]
            copy=dfs(curr*2,curr,c+2)
            notcopy=dfs(curr+i,i,c+1)
            dp[(curr,i)]=min(copy,notcopy)
            return dp[(curr,i)]
        return dfs(1,1,0)