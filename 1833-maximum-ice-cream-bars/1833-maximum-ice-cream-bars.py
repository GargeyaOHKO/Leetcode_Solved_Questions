class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count=[0]*((10**5)+1)
        for i in costs:
            count[i]+=1

        res=0
        for i in range(len(count)):
            if count[i]>0:
                if i*count[i]<=coins:
                    coins-=i*count[i]
                    res+=count[i]
                elif coins//i>0:
                    res+=coins//i
                    coins-=(coins//i)*i
                else:
                    return res
        return res
