class Solution(object):
    def canPartition(self, nums):
        l=[]
        total=sum(nums)
        if total%2!=0:
            return False
        k=total//2
        dp={}
        self.flag=False
        def dfs(i,s):
            if s==k:
                self.flag=True
            if i==len(nums)-1:
                return nums[i]
            if (i,s) in dp:
                return dp[(i,s)]
            if self.flag:
                return True
            take=dfs(i+1,s+nums[i])
            nottake=dfs(i+1,s)
            dp[(i,s)]=take+nottake
            return dp[(i,s)]
        dfs(0,0)
        return self.flag
            
        """
        :type nums: List[int]
        :rtype: bool
        """
        