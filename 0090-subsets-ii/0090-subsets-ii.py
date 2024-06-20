class Solution(object):
    def subsetsWithDup(self, nums):
        res=[]
        l=[]
        def dfs(i):
            if i>=len(nums):
                return None
            else:
                #if l not in res:
                #res.append(list(l))
                l.append(nums[i])
                dfs(i+1)
                if l not in res:
                    res.append(list(l))
                l.pop()
                dfs(i+1)
                if l not in res:
                    res.append((list(l)))
            return res     
        return dfs(0)
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        