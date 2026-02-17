class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        def dfs(i,b):
            if i>=len(prices):
                return 0
            if (i,b) in dp:
                return dp[(i,b)]
            if b==0:
                dp[(i,b)]=max(-prices[i]+dfs(i+1,1),dfs(i+1,b))
            else:
                dp[(i,b)]=max(prices[i]+dfs(i+2,0),dfs(i+1,b))
            return dp[(i,b)]
        return dfs(0,0)
