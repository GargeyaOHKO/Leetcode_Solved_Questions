class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        d=defaultdict(int)
        l=0
        res=0
        for r in range(len(s)):
            d[s[r]]+=1
            while d[s[r]]>2:
                d[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res 