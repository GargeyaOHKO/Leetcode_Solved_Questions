class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    f1,f2=True,True
                    for k in range(len(mat[0])):
                        #print(i,k)
                        if mat[i][k]==1 and k!=j:
                            f1=False
                    for l in range(len(mat)):
                        #print(l,j)
                        if mat[l][j]==1 and l!=i:
                            f2=False
                    if f1==True and f2==True:
                        count+=1
        return count