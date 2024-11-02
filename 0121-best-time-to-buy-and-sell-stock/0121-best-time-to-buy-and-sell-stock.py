class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        pr=0
        for i in range(1,len(prices)):
            pr=max(pr,prices[i]-mini)
            mini=min(mini,prices[i])
        return pr