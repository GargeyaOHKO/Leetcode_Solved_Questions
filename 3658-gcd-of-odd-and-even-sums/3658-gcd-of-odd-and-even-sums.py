class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        o=1
        e=2
        osum,esum=0,0
        i=0
        while i<n:
            osum+=o
            esum+=e
            o+=2
            e+=2
            i+=1
        return math.gcd(osum,esum)
