class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        c=0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                d={"r1":0,"r2":0,"r3":0,"c1":0,"c2":0,"c3":0,"d1":0,"d2":0}
                ds=set()
                flag=True
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if grid[k][l]<1 or grid[k][l]>9:
                            flag=False
                        ds.add(grid[k][l])        
                if len(ds)!=9 or not flag:
                    continue
                else:
                    if( grid[i][j]+grid[i][j+1]+grid[i][j+2]==
                        grid[i+1][j]+grid[i+1][j+1]+grid[i+1][j+2]==
                        grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2]==
                        grid[i][j]+grid[i+1][j]+grid[i+2][j]==
                        grid[i][j+1]+grid[i+1][j+1]+grid[i+2][j+1]==
                        grid[i][j+2]+grid[i+1][j+2]+grid[i+2][j+2]==
                        grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2]==
                        grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]):
                        c+=1
        return c
                