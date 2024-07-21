class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        drow,dcol={},{}
        for i in range(len(grid)):
            row,col=[],[]
            for j in range(len(grid)):
                row.append(str(grid[i][j]))
                col.append(str(grid[j][i]))
            drow[" ".join(row)]=drow.get(" ".join(row),0)+1
            dcol[" ".join(col)]=dcol.get(" ".join(col),0)+1
        c=0
        for i in drow:
            if i in dcol:
                c+=drow[i]*dcol[i]
        return c