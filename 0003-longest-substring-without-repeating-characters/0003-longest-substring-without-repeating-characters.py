class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d=set()
        l,r=0,0
        maxc=0
        while r<len(s):
            while s[r] in d:
                d.remove(s[l])
                l+=1
            d.add(s[r])
            maxc=max(maxc,len(s[l:r+1]))       
            r+=1
        return maxc    