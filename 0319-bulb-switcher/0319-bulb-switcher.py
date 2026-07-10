class Solution:
    def bulbSwitch(self, n: int) -> int:
        c=0
        for i in range(1,100000):
            if i*i<=n:
                c+=1
        return c