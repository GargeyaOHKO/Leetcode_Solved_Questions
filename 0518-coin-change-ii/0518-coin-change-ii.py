class Solution(object):
    def change(self, amount, coins):
        dp={}
        def dfs(i,amt):
            if i==len(coins):
                return 0
            if amt>amount:
                return 0
            if amt==amount:
                return 1
            if (i,amt) in dp:
                return dp[(i,amt)]
            take=dfs(i,amt+coins[i])
            nottake=dfs(i+1,amt)
            dp[(i,amt)]=take+nottake
            return dp[(i,amt)]
        return dfs(0,0)   
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        