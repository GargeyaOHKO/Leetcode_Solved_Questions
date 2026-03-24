class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxi=float('-inf')
        move=[[1,0],[0,1],[-1,0],[0,-1]]
        seen=set()
        def dfs(r,c):
            cnt=1
            for i in move:
                newr,newc=r+i[0],c+i[1]
                if (newr>=0 and newr<len(grid)) and (newc>=0 and newc<len(grid[0])) and grid[newr][newc]==1 and (newr,newc) not in seen:
                    seen.add((newr,newc))
                    cnt+=dfs(newr,newc)
            return cnt

        for i in range(len(grid)):
            count=0
            for j in range(len(grid[0])):
                if grid[i][j]==1 and (i,j) not in seen:
                    #print(i,j)
                    seen.add((i,j))
                    count=dfs(i,j)
                if count!=None and count>maxi:
                    maxi=count
        return maxi
