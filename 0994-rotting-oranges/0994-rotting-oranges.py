class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh=0
        q=deque()
        seen=set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:  
                    q.append([i,j])
                    seen.add((i,j))
        count=0
        #print()
        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                if r+1<len(grid) and grid[r+1][c]==1 and (r+1,c) not in seen:
                    q.append([r+1,c])
                    seen.add((r+1,c))
                    fresh-=1
                if c+1<len(grid[0]) and grid[r][c+1]==1 and (r,c+1) not in seen:
                    q.append([r,c+1])
                    seen.add((r,c+1))
                    fresh-=1
                if r-1>-1 and grid[r-1][c]==1 and (r-1,c) not in seen:
                    q.append([r-1,c])
                    seen.add((r-1,c))
                    fresh-=1
                if c-1>-1 and grid[r][c-1]==1 and (r,c-1) not in seen:
                    q.append([r,c-1])
                    seen.add((r,c-1))
                    fresh-=1
            count+=1
        if fresh!=0:
            return -1
        else:
            return count

