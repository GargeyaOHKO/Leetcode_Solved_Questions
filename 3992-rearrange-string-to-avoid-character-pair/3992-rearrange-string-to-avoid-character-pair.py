class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        d=Counter(s)
        res=""
        for i in range(d[y]):
            res+=y
        for i in range(d[x]):
            res+=x
        del d[x]
        del d[y]
        for i in d:
            for j in range(d[i]):
                res+=i
        return res