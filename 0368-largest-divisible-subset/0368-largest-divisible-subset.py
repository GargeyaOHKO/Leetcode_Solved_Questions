class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp={}
        def dfs(i):
            #print(dp,i)
            if i in dp:
                return dp[i]
            if i>=len(nums):
                return []
            res=[nums[i]]
            for j in range(i+1,len(nums)):
                if nums[j]%nums[i]==0:
                    ans=[nums[i]]+dfs(j)
                    if len(ans)>len(res):
                        res=ans[:]
            dp[i]=res
            return dp[i]

        l=[]
        for i in range(len(nums)):
            temp=dfs(i)
            if len(temp)>len(l):
                l=temp
        return l
        