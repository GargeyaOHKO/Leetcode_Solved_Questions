class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ub=[]
        lb=[]
        for i in range(len(mat[0])):
            ub.append([0,i])
        for i in range(1,len(mat)):
            ub.append([i,len(mat[0])-1])
        
        for i in range(len(mat)):
            lb.append([i,0])
        for i in range(1,len(mat[0])):
            lb.append([len(mat)-1,i])

        l=[]
        for i in range(len(ub)):
            if i%2==0:
                r,c=lb[i]
            else:
                r,c=ub[i]
            while 0<=r<len(mat) and 0<=c<len(mat[0]):
                l.append(mat[r][c])
                if i%2==0:
                    r,c=r-1,c+1                 
                else:
                    r,c=r+1,c-1
        return l

