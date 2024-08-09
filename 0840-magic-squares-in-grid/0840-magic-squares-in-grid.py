class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        c=0
        for k in range(len(grid)-2):
            for l in range(len(grid[0])-2):
                d={"r1":0,"r2":0,"r3":0,"c1":0,"c2":0,"c3":0,"d1":0,"d2":0}
                #print(k,l)
                ds=set()
                flag=True
                for i in range(k,k+3):
                    for j in range(l,l+3):
                        if grid[i][j]>9 or grid[i][j]<1:
                            flag=False
                        ds.add(grid[i][j])
                        if i==0 or k!=0 and i%k==0:
                            d["r1"]+=grid[i][j]
                        if i==1 or k!=0 and i%k==1:
                            d["r2"]+=grid[i][j]
                        if i==2 or k!=0 and i%k==2:
                            d["r3"]+=grid[i][j] 
                        if j==0 or l!=0 and j%l==0:
                            d["c1"]+=grid[i][j]
                        if j==1 or l!=0 and j%l==1:
                            d["c2"]+=grid[i][j]
                        if j==2 or l!=0 and j%l==2:
                            d["c3"]+=grid[i][j]
                        if i==j or l!=0 and k!=0 and i%k==j%l:
                            d["d1"]+=grid[i][j]
                        if i+j==2 or l!=0 and k!=0 and i%k+j%l==2:
                            d["d2"]+=grid[i][j]
                if len(ds)!=9 or not flag:
                    break
                s=set()
                for i in d:
                    if d[i] not in s:
                        #print(i,d[i])
                        s.add(d[i])
                #print(s)
                if len(s)==1:
                    c+=1
        return c
                