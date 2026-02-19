class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums[:]+[1]
        dp={}
        def dfs(l,r):
            #print(l,r)
            if l>r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            score=0
            for i in range(l,r+1):
                score=max(score,nums[l-1]*nums[i]*nums[r+1]+dfs(l,i-1)+dfs(i+1,r))
            dp[(l,r)]=score
            return dp[(l,r)]
        return dfs(1,len(nums)-2)
