class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        res=[[0 for i in range(len(rowSum))]for j in range(len(colSum))]
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                res[i][j]=min(rowSum[i],colSum[j])
                rowSum[i]-=res[i][j]
                colSum[j]-=res[i][j]
        return res