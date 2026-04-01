class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        seen=set()
        def bfs(r,c):
            q=deque()
            q.append((r,c))
            move=[[1,0],[0,1],[-1,0],[0,-1]]
            cnt=1
            while q:
                for i in range(len(q)):
                    r,c=q.popleft()
                    for j in move:
                        newr,newc=j[0]+r,j[1]+c
                        if 0<=newr<len(grid) and 0<=newc<len(grid[0]) and grid[newr][newc]==1 and (newr,newc) not in seen:
                            cnt+=1
                            q.append([newr,newc])
                            seen.add((newr,newc))
            return cnt
                    
        c=0
        total=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and (i==0 or i==len(grid)-1 or j==0 or j==len(grid[0])-1) and (i,j) not in seen:
                    seen.add((i,j))
                    c=c+bfs(i,j)
                if grid[i][j]==1:
                    total+=1
        return total-c
        
