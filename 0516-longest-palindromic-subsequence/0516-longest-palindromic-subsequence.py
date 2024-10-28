class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp={}
        def dfs(l,r):
            if r<l:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            if s[l]==s[r] and l==r:
                dp[(l,r)]=1+dfs(l+1,r-1)
                return dp[(l,r)]
            elif s[l]==s[r]:
                dp[(l,r)]=2+dfs(l+1,r-1)
                return dp[(l,r)]
            else:
                dp[(l,r)]=max(dfs(l+1,r),dfs(l,r-1))
                return dp[(l,r)]

        return dfs(0,len(s)-1)
        