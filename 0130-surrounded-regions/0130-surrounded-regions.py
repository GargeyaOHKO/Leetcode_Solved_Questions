class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q=deque()
        seen=set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i==0 or j==0 or i==len(board)-1 or j==len(board[0])-1) and board[i][j]=="O":
                    q.append([i,j])
                    seen.add((i,j))
        moves=[[0,1],[1,0],[-1,0],[0,-1]]
        while q:
            for i in range(len(q)):
                curr=q.popleft()
                for m in moves:
                    newr,newc=curr[0]+m[0],curr[1]+m[1]
                    if 0<=newr<len(board) and 0<=newc<len(board[0]) and (newr,newc) not in seen and board[newr][newc]=="O":
                        q.append([newr,newc])
                        seen.add((newr,newc))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="O" and (i,j) not in seen:
                    board[i][j]="X"
        