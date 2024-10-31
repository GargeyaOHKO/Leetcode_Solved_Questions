class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp={}
        def dfs(i,j,k):
            if (i,j,k) in dp:
                return dp[(i,j,k)]
            if i==len(s1) and j==len(s2) and k==len(s3):
                return True
            if k==len(s3):
                return False
            else:
                f1,f2=False,False
                if i<len(s1) and s1[i]==s3[k]:
                    f1=dfs(i+1,j,k+1)
                if j<len(s2) and s2[j]==s3[k]:
                    f2=dfs(i,j+1,k+1)
                dp[(i,j,k)]=f1 or f2
                return dp[(i,j,k)]
        return dfs(0,0,0)
        
        