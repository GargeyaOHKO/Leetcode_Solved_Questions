class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        moves=[[1,0],[0,1],[-1,0],[0,-1]]
        close=[[500 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        q=deque()
        seen=set()
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j]==1:
                    q.append([i,j])
                    close[i][j]=0
                    seen.add((i,j))
        cnt=1
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                for m in moves:
                    newr,newc=r+m[0],c+m[1]
                    if 0<=newr<len(grid) and 0<=newc<len(grid) and (newr,newc) not in seen:
                        close[newr][newc]=cnt
                        q.append([newr,newc])
                        seen.add((newr,newc))
            cnt+=1
        #print(close)

        h=[[-close[0][0],0,0]]
        s=set()
        mini=float('inf')
        while h:
            val,r,c=heapq.heappop(h)
            mini=min(mini,-val)
            if r==len(grid)-1 and c==len(grid)-1:
                return mini
            if (r,c) in s:
                continue 
            s.add((r,c))
            for m in moves:
                newr,newc=r+m[0],c+m[1]
                if 0<=newr<len(grid) and 0<=newc<len(grid) and (newr,newc) not in s:
                    heapq.heappush(h,[-close[newr][newc],newr,newc])
