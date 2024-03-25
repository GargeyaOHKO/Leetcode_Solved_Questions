class Solution(object):
    def numberOfSubstrings(self, s):
        d={"a":0,"b":0,"c":0}
        l,r=0,0
        maxc=0
        while r<len(s):
            d[s[r]]+=1
            while d["a"]>=1 and d["b"]>=1 and d["c"]>=1:
                maxc+=len(s)-r
                d[s[l]]-=1
                l+=1
            r+=1      
        return maxc
        """
        :type s: str
        :rtype: int
        """
        