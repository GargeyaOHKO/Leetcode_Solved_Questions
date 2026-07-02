class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        moves=[[1,0],[0,1],[-1,0],[0,-1]]
        seen=set()
        if grid[0][0]==1:
            health-=1
        h=[[grid[0][0],-health,0,0,]]
        while h:
            #print(h)
            val,health,r,c=heapq.heappop(h)
            health=abs(health)
            #print(r,c,health)
            if r==len(grid)-1 and c==len(grid[0])-1 and health>0:
                return True
            if ((r,c) in seen) or health<1:
                continue
            seen.add((r,c))
            for m in moves:
                newr,newc=r+m[0],c+m[1]
                th=health
                if 0<=newr<len(grid) and 0<=newc<len(grid[0]) and (newr,newc) not in seen:
                    if grid[newr][newc]==1:
                        heapq.heappush(h,[grid[newr][newc],-(th-1),newr,newc])
                    else:
                        heapq.heappush(h,[grid[newr][newc],-(th),newr,newc])
        return False