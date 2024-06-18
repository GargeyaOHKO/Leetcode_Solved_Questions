class Solution(object):
    def combinationSum(self, candidates, target): 
        import itertools
        res=[]
        l=[]
        def dfs(i):
            if i>=len(candidates) or sum(l)>target:
                return None
            if sum(l)==target:
                res.append(list(l))
                return None
            l.append(candidates[i])
            dfs(i)
            l.pop()
            dfs(i+1)
            return res
        return dfs(0)       
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        