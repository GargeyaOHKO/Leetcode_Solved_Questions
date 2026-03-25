class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        vpref,vsuff=[],[]
        hpref,hsuff=[],[]
        s=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                s+=grid[i][j]
            hpref.append(s)
        s=0
        for i in range(len(grid)-1,-1,-1):
            for j in range(len(grid[0])-1,-1,-1):
                s+=grid[i][j]
            hsuff.append(s)
        hpref.pop()
        hsuff.pop()
        #print(hpref,hsuff)
        for i in range(len(hpref)):
            if hpref[i]==hsuff[-1-i]:
                return True
        
        s=0
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                s+=grid[j][i]
            vpref.append(s)
        s=0
        for i in range(len(grid[0])-1,-1,-1):
            for j in range(len(grid)-1,-1,-1):
                s+=grid[j][i]
            vsuff.append(s)
        vpref.pop()
        vsuff.pop()
        #print(vpref,vsuff)
        for i in range(len(vpref)):
            if vpref[i]==vsuff[-1-i]:
                return True
        return False

            
        