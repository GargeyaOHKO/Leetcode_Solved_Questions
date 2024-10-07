class Solution:
    def minLength(self, s: str) -> int:
        l=0
        while l<len(s)-1:
            #print(l,s)
            if len(s)==0:
                return 0
            if (s[l]=="A" and s[l+1]=="B") or (s[l]=="C" and s[l+1]=="D"):
                if (l+2)<len(s):
                    s=s[:l]+s[l+2:]
                else:
                    s=s[:l]
                    l=len(s)-2
                if l>0:
                    l-=1
            else:
                l+=1
        return len(s)

