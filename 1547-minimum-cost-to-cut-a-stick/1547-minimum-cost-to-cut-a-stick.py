class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        dp={}
        def dfs(i,j):
            if j-i==0:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            cost=float('inf')
            for c in cuts:
                if c<j and i<c:
                    cost=min(cost,(j-i)+dfs(i,c)+dfs(c,j))
            if cost!=float('inf'):
                dp[(i,j)]=cost
            else:
                dp[(i,j)]=0
            return dp[(i,j)]
        return dfs(0,n)
                