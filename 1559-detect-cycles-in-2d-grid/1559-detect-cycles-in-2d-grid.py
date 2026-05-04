class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        globalseen=set()

        def dfs(a,b):
            moves=[[0,1],[1,0],[-1,0],[0,-1]]
            q=deque()
            q.append([a,b,-1,-1])
            seen=set()
            seen.add((a,b))
            globalseen.add((a,b))
            while q:
                for i in range(len(q)):
                    #print(q,"seen",seen,"gseen",globalseen)
                    r,c,prevr,prevc=q.popleft()
                    for m in moves:
                        newr,newc=r+m[0],c+m[1]
                        #print(newr,newc,prevr,prevc)
                        if 0<=newr<len(grid) and 0<=newc<len(grid[0]) and (newr,newc) not in seen and grid[newr][newc]==grid[r][c]:
                            q.append([newr,newc,r,c])
                            seen.add((newr,newc))
                            globalseen.add((newr,newc))
                        elif (newr,newc) in seen and (newr!=prevr or newc!=prevc):
                            return True

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in globalseen:
                    if dfs(r,c):
                        return True

        return False