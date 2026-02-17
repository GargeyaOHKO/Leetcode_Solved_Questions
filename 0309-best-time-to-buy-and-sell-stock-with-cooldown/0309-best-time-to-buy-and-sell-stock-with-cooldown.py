class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        def dfs(i,buyp):
            #print(i,buyp,profit)
            if i>=len(prices):
                return 0
            if (i,buyp) in dp:
                return dp[(i,buyp)]
            if buyp!=-1:
                dp[(i,buyp)]=max(prices[i]+dfs(i+2,-1),dfs(i+1,buyp))
            else:
                dp[(i,buyp)]=max(-prices[i]+dfs(i+1,prices[i]),dfs(i+1,-1))
            return dp[(i,buyp)]
        return dfs(0,-1)


