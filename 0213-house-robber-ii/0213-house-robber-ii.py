class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[-1]*len(nums)
        def dfs(start,i):
            if start==0 and i==len(nums)-2:
                return nums[-2]
            if start==0 and i>=len(nums)-1:
                return 0 
            if start!=0 and i==len(nums)-1:
                return nums[-1]
            if start!=0 and i>=len(nums):
                return 0
            if dp[i]!=-1:
                return dp[i]
            take=nums[i]+dfs(i,i+2)
            nottake=dfs(i+1,i+1)
            dp[i]=max(take,nottake)
            return dp[i]
        return dfs(0,0)

