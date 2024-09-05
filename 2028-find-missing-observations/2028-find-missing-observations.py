class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        s=sum(rolls)
        val=(mean*(len(rolls)+n))-s
        l=[0]*n
        if (s+n)//(len(rolls)+n)>mean:
            return []
        if val>n*6:
            return []
        for i in range(val):
            l[i%n]+=1
        return l