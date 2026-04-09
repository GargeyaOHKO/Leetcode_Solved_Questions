class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        moves=[[0,1],[1,0],[-1,0],[0,-1]]
        inbound=[[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        q=deque()
        seen=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ib=0
                for m in moves:
                    newr,newc=i+m[0],j+m[1]
                    if 0<=newr<len(matrix) and 0<=newc<len(matrix[0]) and matrix[i][j]>matrix[newr][newc]:
                        ib+=1
                inbound[i][j]=ib
                if ib==0:
                    q.append([i,j])
                    seen.add((i,j))
        c=0
        while q:
            for i in range(len(q)):
                curr=q.popleft()
                for m in moves:
                    newr,newc=curr[0]+m[0],curr[1]+m[1]
                    if 0<=newr<len(matrix) and 0<=newc<len(matrix[0]) and matrix[curr[0]][curr[1]]<matrix[newr][newc]:
                        inbound[newr][newc]-=1
                        if inbound[newr][newc]==0:
                            q.append([newr,newc])
            c+=1
        return c 