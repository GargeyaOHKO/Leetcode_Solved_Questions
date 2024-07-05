class Solution(object):
    def findTargetSumWays(self, nums, target):
        n=len(nums)
        dp={}
        def dfs(i,s):
            if i==n:
                if s==target:
                    return 1
                else:
                    return 0
            if (i,s) in dp:
                return dp[(i,s)]
            dp[(i,s)]=dfs(i+1,s+nums[i])+dfs(i+1,s-nums[i])
            return dp[(i,s)]  
        return dfs(0,0)
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        