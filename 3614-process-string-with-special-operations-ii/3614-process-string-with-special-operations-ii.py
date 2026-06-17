class Solution:
    def processStr(self, s: str, k: int) -> str:
        l=0
        for i in s:
            if i=="*":
                l=max(0,l-1)
            elif i=="#":
                l*=2
            elif i=="%":
                pass
            else:
                l+=1

        if k>l-1:
            return "."

        for i in reversed(s):
            #print(l,k,i)
            if i=="*":
                l+=1
            elif i=="%":
                k=l-k-1
            elif i=="#":
                l//=2
                if k>=l:
                    k-=l
            else:
                if l-1==k:
                    return i
                l-=1