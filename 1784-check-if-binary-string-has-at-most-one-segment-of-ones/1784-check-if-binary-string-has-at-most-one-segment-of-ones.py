class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if s[0]!="1":
            return False
        f=False
        for i in range(1,len(s)):
            if s[i]=='0':
                f=True
            if s[i]=='1' and f==True:
                return False
        return True