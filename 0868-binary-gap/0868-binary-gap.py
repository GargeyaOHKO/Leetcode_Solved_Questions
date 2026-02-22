class Solution:
    def binaryGap(self, n: int) -> int:
        b=bin(n)[2:]
        l,r=0,0
        m,c=0,0
        while l<len(b):
            if b[l]=='1':
                m=max(m,c)
                r=l
                l+=1
                c=1
            else:
                l+=1
                c+=1
        return m