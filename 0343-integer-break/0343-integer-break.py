class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=3:
            return n-1 
        self.max=0
        dp={}
        def dfs(n,prod):
            #print(n,prod)
            if (n,prod) in dp:
                return dp[(n,prod)]
            if n<=0:
                return prod
            l=[]
            for i in range(1,n+1):
                pr=dfs(n-i,prod*i)
                l.append(pr)
            dp[(n,prod)]=max(l)
            return dp[(n,prod)]
        return dfs(n,1)

                   
