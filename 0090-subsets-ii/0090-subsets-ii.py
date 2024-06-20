class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        res=[]
        def dfs(i,l):
            if i>=len(nums):
                res.append(list(l))
                return None
            else:
                l.append(nums[i])
                dfs(i+1,l)
                l.pop()
                while i+1<len(nums) and nums[i]==nums[i+1]:
                    i+=1
                dfs(i+1,l)
            return res     
        return dfs(0,[])
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        