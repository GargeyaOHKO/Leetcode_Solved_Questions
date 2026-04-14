class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        moves=[[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1]]
        q=deque()
        seen=set()
        if len(grid)==1 and grid[0][0]==0:
            return 1
        if grid[0][0]==0:
            q.append([0,0])
            seen.add((0,0))
        c=1
        while q:
            #print(q)
            c+=1
            for i in range(len(q)):
                curr=q.popleft()
                for m in moves:
                    newr,newc=curr[0]+m[0],curr[1]+m[1]
                    if 0<=newr<len(grid) and 0<=newc<len(grid) and (newr,newc) not in seen and grid[newr][newc]==0:
                        q.append([newr,newc])
                        seen.add((newr,newc))
                        if newr==len(grid)-1 and newc==len(grid[0])-1:
                            return c
        return -1
