class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d1=Counter(p)
        d2={}
        l=0
        res=[]
        for i in range(len(s)):
            #print(d1,d2)
            if i>=len(p):
                d2[s[l]]-=1
                if d2[s[l]]==0:
                    del d2[s[l]]
                l+=1
            d2[s[i]]=d2.get(s[i],0)+1
            if d1==d2:
                res.append(l)
        return res
