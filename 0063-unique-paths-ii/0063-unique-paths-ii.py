class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        n,m=len(obstacleGrid),len(obstacleGrid[0])
        dp=[[-1 for i in range(m)]for j in range(n)]
        def dfs(i,j):
            if i<0 or j<0 or i>=n or j>=m:
                return 0
            if obstacleGrid[i][j]==1:
                return 0
            if i==n-1 and j==m-1:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            right=dfs(i+1,j)
            left=dfs(i,j+1)
            dp[i][j]=right+left
            return dp[i][j]
        return dfs(0,0)
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        