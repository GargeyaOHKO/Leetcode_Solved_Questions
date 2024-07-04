class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        dp=[[[-1 for i in range(maxMove)] for j in range(m+1)] for k in range(n+1)]
        def dfs(i,j,move):
            if (i<0 or j<0 or i>=m or j>=n) and move<=maxMove:
                return 1
            if move>maxMove:
                return 0
            if dp[move][i][j]!=-1:
                return dp[move][i][j]

            left=dfs(i,j-1,move+1)
            right=dfs(i,j+1,move+1)
            up=dfs(i-1,j,move+1)
            down=dfs(i+1,j,move+1)

            res=left+right+up+down
            dp[move][i][j]=res
            return res
        res=dfs(startRow,startColumn,0)
        return (res%(10**9+7))
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        