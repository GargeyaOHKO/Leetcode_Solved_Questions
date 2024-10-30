class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def dfs(i,j):
            if i==len(s) and j==len(p):
                return True
            elif i==len(s) and j<len(p):
                f=True
                for z in range(j,len(p)):
                    if p[z]!='*':
                        f=False
                return f
            elif i<len(s) and j==len(p):
                    return False

            if s[i]==p[j] or p[j]=="?":
                return dfs(i+1,j+1)
            elif p[j]=="*":
                return dfs(i,j+1)|dfs(i+1,j)
            else:
                return False
        return dfs(0,0)