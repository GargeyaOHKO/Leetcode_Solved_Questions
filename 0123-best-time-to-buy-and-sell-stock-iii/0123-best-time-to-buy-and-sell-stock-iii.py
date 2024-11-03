class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        def dfs(i,b,count):
            if (i,b,count) in dp:
                return dp[(i,b,count)]
            if i==len(prices) or count==4:
                return 0
            if b==0:
                dp[(i,b,count)]=max(-prices[i]+dfs(i+1,1,count+1), dfs(i+1,b,count))
            else:
                dp[(i,b,count)]=max(prices[i]+dfs(i+1,0,count+1), dfs(i+1,b,count))
            return dp[(i,b,count)]
        return dfs(0,0,0)