class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols=len(board),len(board[0])
        s=set()
        self.flag=False

        def dfs(r,c,i):
            if i==len(word):
                #print(True)
                self.flag=True
                return None
            if r<0 or c<0 or r>=rows or c>=cols or (r,c) in s:
                return None
            #print(board[r][c])
            if board[r][c]==word[i]:
                #print(word[i],i)
                s.add((r,c))
                dfs(r+1,c,i+1)
                dfs(r,c+1,i+1) 
                dfs(r,c-1,i+1)
                dfs(r-1,c,i+1)
                s.remove((r,c))    
            return None
        
        for i in range(rows):
            for j in range(cols):
                dfs(i,j,0)
        return self.flag