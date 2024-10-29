class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        @lru_cache(maxsize=20000)
        def dfs(i,j):
            if not i and not j:
                return ""
            if not i:
                return j
            if not j:
                return i
            if i[0]==j[0]:
                return i[0]+dfs(i[1:],j[1:])
            else:
                p1=i[0]+dfs(i[1:],j)
                p2=j[0]+dfs(i,j[1:])
                if len(p1)<len(p2):
                    return p1
                elif len(p1)>len(p2):
                    return p2
                else:
                    return min(p1,p2)
        return dfs(s1,s2)
                
        