class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(l,openn,close):
            if openn==n and close==n:
                res.append(str(l))
                return None
            if openn<n:
                l+="("
                dfs(l,openn+1,close)
                l=l[:-1]
            if close<openn:
                l+=")"
                dfs(l,openn,close+1)
            return res
        return dfs("",0,0)