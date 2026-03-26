class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        res=[[float('inf') for i in range(len(mat[0]))] for j in range(len(mat))]
        q=deque()
        seen=set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    q.append([i,j])
                    seen.add((i,j))
                    res[i][j]=0
        move=[[1,0],[0,1],[-1,0],[0,-1]]
        c=1
        while q:
            for i in range(len(q)):
                k=q.popleft()
                for j in move:
                    newr,newc=k[0]+j[0],k[1]+j[1]
                    if 0<=newr<len(mat) and 0<=newc<len(mat[0]) and (newr,newc) not in seen:
                        res[newr][newc]=c
                        q.append([newr,newc])
                        seen.add((newr,newc))
            c+=1
        return res