class Solution:
    def minimumDeletions(self, s: str) -> int:
        prevb=[0 for i in range(len(s))]
        nexta=[0 for i in range(len(s))]
        c=0
        for i in range(len(s)):
            prevb[i]=c
            if s[i]=='b':
                c+=1
        m=float('inf')
        c=0
        for i in range(len(s)-1,-1,-1):
            m=min(m,c+prevb[i])
            if s[i]=='a':
                c+=1
        return m