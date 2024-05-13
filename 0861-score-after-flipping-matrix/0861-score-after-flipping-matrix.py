class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for i in grid:
            if i[0]!=1:
                for j in range(len(i)):
                    if i[j]==0:
                        i[j]=1
                    else:
                        i[j]=0
        for i in range(len(grid[0])):
            d={0:0,1:0}
            for j in range(len(grid)):
                d[grid[j][i]]=d.get(grid[j][i],0)+1
            #print(d)    
            if d[0]>d[1]:
                x=i
                for y in range(len(grid)):
                    if grid[y][x]==1:
                        grid[y][x]=0
                    else:
                        grid[y][x]=1
        c=0
        for i in grid:
            s=""
            for j in i:
                s+=str(j)       
            c+=int(s, 2)          
        return c                 

        