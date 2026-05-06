class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        seen=set()
        self.flag=False
        def dfs(r,c,prevr,prevc):
            moves=[[0,1],[1,0],[0,-1],[-1,0]]
            for m in moves:
                newr,newc=r+m[0],c+m[1]
                if 0<=newr<len(grid) and 0<=newc<len(grid[0]) and grid[newr][newc]==grid[r][c] and (newr,newc) not in seen:
                    #print(newr,newc,prevr,prevc)
                    seen.add((newr,newc))
                    dfs(newr,newc,r,c)
                elif (newr,newc) in seen and (newr!=prevr or newc!=prevc) and grid[newr][newc]==grid[r][c]:
                    #print("final",newr,newc,prevr,prevc)
                    self.flag=True
                    return True

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                #print("initial",r,c)
                if (r,c) not in seen:
                    seen.add((r,c))
                    if dfs(r,c,-1,-1):
                        return True
        return self.flag
        return False