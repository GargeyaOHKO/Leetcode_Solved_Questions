class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        l,r=0,0
        maxc=0
        while r<len(s):
            while s[r] in d:
                del[d[s[l]]]
                l+=1
            else:
                d[s[r]]=1
            maxc=max(maxc,len(s[l:r+1]))       
            r+=1
        return maxc    