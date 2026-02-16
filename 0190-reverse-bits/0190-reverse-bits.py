class Solution:
    def reverseBits(self, n: int) -> int:
        s=""
        for i in range(32-1,-1,-1):
            if n>=2**i:
                s="1"+s
                n-=2**i
            else:
                s="0"+s
        ans=0
        power=31
        for i in range(len(s)):
            if s[i]=="1":
                ans+=2**power
            power-=1
        return ans




