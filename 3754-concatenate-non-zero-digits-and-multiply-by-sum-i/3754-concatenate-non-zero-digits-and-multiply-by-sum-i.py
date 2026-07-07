class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=str(n)
        news="0"
        sumo=0
        for i in s:
            if i!="0":
                news+=i
                sumo+=int(i)
        return int(news)*sumo
