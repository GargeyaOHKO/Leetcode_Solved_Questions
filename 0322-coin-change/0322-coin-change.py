class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp={}
        l=[]
        def dfs(index,amount,number):
            if index==0:
                if amount%coins[index]==0:
                    return amount//coins[index]
                return float('inf')
            if amount<0 or index<0:
                return float('inf')
            if (amount,number) in dp:
                return dp[(amount,number)]
            tot = float('inf')
            dp[(amount,number)]=min(pick,notpick)
            return dp[(amount,number)]
        num=dfs(0,amount,0)
        if num==float("inf"):
            return -1
        else:
           return num
 
