class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort()
        c=0
        for i in prices:    
            if discounts:
                c+=(i*(100-discounts.pop())/100)
            else:
                c+=i
        return c