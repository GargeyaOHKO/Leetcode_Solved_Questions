class Solution(object):
    def minimumTotal(self, triangle):
        height=len(triangle)
        dp=[[-1 for i in range(height)] for j in range(height)]

        def dfs(i,j):
            #print(dp)
            if i<0 or j<0 or i>=height or j>i:
                return float('inf')
            if i==height-1:
                return triangle[i][j]
            if dp[i][j]!=-1:
                return dp[i][j]
            left=dfs(i+1,j)
            right=dfs(i+1,j+1)
            dp[i][j]=triangle[i][j]+min(left,right)
            return dp[i][j]
        return dfs(0,0)
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        