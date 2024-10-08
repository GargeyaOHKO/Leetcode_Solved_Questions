class Solution:
    def minSwaps(self, s: str) -> int:
        b=len(s)-1
        ob,cb=0,0
        swap=0
        l=list(s)
        for i in range(len(s)):
            #print(l)
            if l[i]=="]":
                cb+=1
            elif l[i]=="[":
                ob+=1
            #print(cb,ob)
            if cb>ob:
                while l[b]!='[':
                    b-=1
                l[i],l[b]=l[b],l[i]
                cb-=1
                ob+=1
                swap+=1
        return swap    