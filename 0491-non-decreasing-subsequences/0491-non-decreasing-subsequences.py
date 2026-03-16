class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        def dfs(i,l):
            if i>=len(nums):
                if len(l)>1 and l not in self.res:
                    self.res.append(l)
                return 0
            if l==[] or nums[i]>=l[-1]:
                dfs(i+1,l)
                dfs(i+1,l+[nums[i]])
            else:
                dfs(i+1,l)
        dfs(0,[])
        return self.res
