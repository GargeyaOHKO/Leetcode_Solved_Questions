class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        for i in range(len(nums)):
            mini=0
            for j in range(i):
                if nums[j]<nums[i]:
                    mini=max(mini,dp[j])
            dp[i]+=mini
        return max(dp)