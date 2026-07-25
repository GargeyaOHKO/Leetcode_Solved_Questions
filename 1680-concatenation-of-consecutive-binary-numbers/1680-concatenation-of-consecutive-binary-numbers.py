class Solution:
    def concatenatedBinary(self, n: int) -> int:
        s=0
        for i in range(1,n+1):
            new=bin(i)[2:]
            s=((s<<len(new))+i)%(10**9+7)
        return s
        

