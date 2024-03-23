class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        l,r=0,0
        maxc=0
        for i in s:
            if i not in d:
                d[i]=0
        for r in range(len(s)):
            d[s[r]]+=1
            if (r-l+1)-max(d.values())>k:
                d[s[l]]-=1
                l+=1
            maxc=max(maxc,r-l+1)    
        return maxc

         
        