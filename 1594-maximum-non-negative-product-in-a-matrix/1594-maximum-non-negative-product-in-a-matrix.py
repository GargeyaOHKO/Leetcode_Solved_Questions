class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        self.maxprod=float('-inf')
        dp={}
        def dfs(r,c,res):
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]):
                return -1
            if r==len(grid)-1 and c==len(grid[0])-1:
                self.maxprod=max(self.maxprod,res*grid[r][c])
            if (r,c,res) in dp:
                return dp[(r,c,res)]
            #print(r,c,res)
            dp[(r,c,res)]=max(dfs(r,c+1,res*grid[r][c]),dfs(r+1,c,res*grid[r][c]))
            return dp[(r,c,res)]
        dfs(0,0,1)
        if self.maxprod<0:
            return -1
        else:
            return self.maxprod%(10**9+7)