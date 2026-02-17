class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(i,total,dp):
            if i>=len(cost):
                return total
            if i in dp:
                return dp[i]
            total+=cost[i]+min(dfs(i+1,total,dp),dfs(i+2,total,dp))
            dp[i]=total
            return dp[i]
        s1=dfs(0,0,{})
        s2=dfs(1,0,{})
        return min(s1,s2)
        