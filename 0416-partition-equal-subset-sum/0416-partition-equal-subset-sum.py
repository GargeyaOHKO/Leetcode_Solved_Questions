class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s&1==1:
            return False
        else:
            s=s//2
        dp={}
        def dfs(i,c1,c2):
            if (i,c1,c2) in dp:
                return dp[(i,c1,c2)]
            if i==len(nums):
                if c1==c2:
                    return True
                else:
                    return False
            dp[(i,c1,c2)]=dfs(i+1,c1+nums[i],c2) or dfs(i+1,c1,c2+nums[i])
            return dp[(i,c1,c2)]
        return dfs(0,0,0)