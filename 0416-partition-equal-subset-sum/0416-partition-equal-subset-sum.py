class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s&1==1:
            return False
        else:
            s=s//2
        dp={}
        def dfs(i,c):
            if (i,c) in dp:
                return dp[(i,c)]
            if i==len(nums):
                return False
            if c==s:
                return True
            dp[(i,c)]=dfs(i+1,c+nums[i])|dfs(i+1,c)
            return dp[(i,c)]
        return dfs(0,0)