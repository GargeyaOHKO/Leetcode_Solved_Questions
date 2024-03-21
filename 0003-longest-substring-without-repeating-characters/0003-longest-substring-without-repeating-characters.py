class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        l,r=0,0
        c,maxc=0,0
        while r<len(s) and l<=r:
            if s[r] not in d:
                d[s[r]]=1
                c+=1
                r+=1
            elif s[r] in d and l<len(s)-1:       
                l+=1
                r=l
                d={}
                d[s[r]]=1
                c=1
                r+=1              
            maxc=max(maxc,c)       
        return maxc    

