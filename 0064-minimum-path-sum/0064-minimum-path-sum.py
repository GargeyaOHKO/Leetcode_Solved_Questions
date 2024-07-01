class Solution(object):
    def minPathSum(self, grid):
        m,n=len(grid),len(grid[0])
        dp=[[-1 for i in range(n)]for j in range(m)]
        l=[]
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n:
                return float('inf')
            if i==m-1 and j==n-1:
                return grid[i][j]
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j]=grid[i][j]+min(dfs(i,j+1),dfs(i+1,j))
            return dp[i][j]
        return dfs(0,0)

        """
        :type grid: List[List[int]]
        :rtype: int
        """
        