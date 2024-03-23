class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        l=0
        maxc=0
        for r in range(len(s)):
            while s[r] in d:
                del(d[s[l]])
                l+=1
            d[s[r]]=1
            maxc=max(maxc,len(s[l:r+1]))    
        return maxc    

