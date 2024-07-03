class Solution(object):
    def minFallingPathSum(self, matrix):
        n=len(matrix)
        memo={}
        def dfs(i,j):
            if i<0 or j<0 or i>=n or j>=n:
                return float('inf')
            if i==n-1:
                return matrix[i][j]
            if (i,j) in memo:
                return memo[(i,j)]
            mid=matrix[i][j]+dfs(i+1,j)
            left=matrix[i][j]+dfs(i+1,j-1)
            right=matrix[i][j]+dfs(i+1,j+1)
            res=min(mid,min(left,right))
            memo[(i,j)]=res
            return res

        mini=float('inf')
        for i in range(n):
            mini=min(mini,dfs(0,i))
        return mini
        """
        :type matrix: List[List[int]]
        :rtype: int
        """