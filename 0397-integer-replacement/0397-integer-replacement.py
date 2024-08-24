class Solution:
    def integerReplacement(self, n: int) -> int:
        dp={}
        def dfs(n,c):
            if n==1:
                return c
            if n<0:
                return float('inf')
            if (n,c) in dp:
                return dp[(n,c)]
            if n%2==0:
                a=dfs(n//2,c+1)
                dp[(n,c)]=a
            else:
                add=dfs((n+1)//2,c+2)
                sub=dfs((n-1)//2,c+2)
                dp[(n,c)]=min(add,sub)
            return dp[(n,c)]
        return dfs(n,0)
                

        