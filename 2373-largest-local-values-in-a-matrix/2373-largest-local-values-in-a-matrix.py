class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        fl=[]
        n=len(grid)
        for a in range(len(grid)-2):
            l=[]
            for b in range(len(grid)-2):
                maxi=0
                for i in range(a,a+3):
                    for j in range(b,b+3):
                        maxi=max(maxi,grid[i][j])
                l.append(maxi)        
            fl.append(l)
        return fl            


        