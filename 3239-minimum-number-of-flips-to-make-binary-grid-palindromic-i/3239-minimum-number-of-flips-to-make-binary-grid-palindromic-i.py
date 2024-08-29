class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        c1=0
        for i in grid:
            l,r=0,len(i)-1
            while l<r:
                if i[l]!=i[r]:
                    c1+=1
                l+=1
                r-=1
        c2=0
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                #print(i,j,end=" ")
                #print()
                if j<(len(grid)-j-1):
                    #print(j,len(grid[i])-j-1)
                    #print(grid[j][i],grid[len(grid[i])-j-1][i])
                    if grid[j][i]!=grid[len(grid)-j-1][i]:
                        c2+=1
            #print()
        return min(c1,c2)