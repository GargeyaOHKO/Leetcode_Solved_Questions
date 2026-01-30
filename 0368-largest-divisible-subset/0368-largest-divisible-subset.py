class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp={}
        def dfs(i,last):
            if (i,last) in dp:
                return dp[(i,last)]
            if i>=len(nums):
                return []
            skip=dfs(i+1,last)
            if nums[i]%last==0:
                take=[nums[i]]+dfs(i+1,nums[i])
                if len(take)>len(skip):
                    skip=take
            dp[(i,last)]=skip
            return dp[(i,last)]
        return dfs(0,1)
        