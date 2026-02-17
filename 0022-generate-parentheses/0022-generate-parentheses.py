class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(o,c,s):
            if len(s)==2*n:
                res.append(s)
                return 0
            if o>0:
                s+='('
                dfs(o-1,c+1,s)
                s=s[:len(s)-1]
            if c>0:
                s+=')'
                dfs(o,c-1,s)
                s=s[:len(s)-1]
        dfs(n-1,1,"(")
        return res