class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        res=[]
        l=[]
        def dfs(i):
            if i>=len(nums):
                if l not in res:
                    res.append(list(l))
                return None
            else:
                l.append(nums[i])
                dfs(i+1)
                l.pop()
                dfs(i+1)
            return res     
        return dfs(0)
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        