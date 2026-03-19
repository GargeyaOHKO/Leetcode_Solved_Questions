class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        res=[]
        for i in range(len(grid)):
            l=[]
            x,y=0,0
            for j in range(len(grid[0])):
                if grid[i][j]=="X":
                    x+=1
                elif grid[i][j]=="Y":
                    y+=1
                l.append([x,y])
            res.append(l)
        
        #print(res)
        fres=[[] for i in range(len(res))]
        #print(fres)
        for i in range(len(grid[0])):
            l=[]
            x,y=0,0
            for j in range(len(grid)):
                #print(res[j][i])
                x+=res[j][i][0]
                y+=res[j][i][1]
                fres[j].append([x,y])
        #print(fres)
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                x,y=fres[i][j][0],fres[i][j][1]
                if x>0 and y==x:
                    count+=1
        return count 
                 