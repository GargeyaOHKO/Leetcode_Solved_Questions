class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp={0:0}
        def dfs(amt):
            if amt in dp:
                return dp[amt]
            mini=float('inf')
            for c in coins:
                diff=amt-c
                if diff<0:
                    break
                mini=min(mini,1+dfs(diff))
            dp[amt]=mini
            return dp[amt]
        num=dfs(amount)
        if num==float("inf"):
            return -1
        else:
           return num
 
