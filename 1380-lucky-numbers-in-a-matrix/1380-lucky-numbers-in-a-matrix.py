class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rowmin=[]
        colmax=[]
        for i in range(len(matrix)):
            rowmin.append(min(matrix[i]))
        #print(rowmin)
        for i in range(len(matrix[0])):
            maxc=0
            for j in range(len(matrix)):    
                maxc=max(maxc,matrix[j][i])
            colmax.append(maxc)
        #print(colmax)
        res=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                #print(matrix[i][j],rowmin[i],colmax[i])
                if matrix[i][j]==rowmin[i] and matrix[i][j]==colmax[j]:
                    res.append(matrix[i][j])
        return res