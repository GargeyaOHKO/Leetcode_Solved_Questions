class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                b=format(grid[i][j], '020b')
                grid[i][j]=b
        news=""
        for z in range(0,20):
            f=True
            for i in range(m):
                #print(grid[i],z)
                s=set()
                for j in range(n):
                    #print(grid[i][j][z])
                    if grid[i][j][0]!='.':
                        b=grid[i][j][z]
                        s.add(b)
                #print(s)
                if '1' in s and '0' not in s:
                    f=False
                    break
                elif '0' in s and '1' not in s:
                    for j in range(n):
                        if grid[i][j][z]=='1':
                            grid[i][j]='.'+grid[i][j][1:]
            #print(f)
            if not f:
                news+='1'
            else:
                news+='0'
                for i in range(m):
                    for j in range(n):
                        if grid[i][j][z]=='1':
                            grid[i][j]='.'+grid[i][j][1:]
            #print(news)
        #print(news)
        return int(news,2)
