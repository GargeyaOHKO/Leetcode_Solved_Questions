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
            l.append(candidates[i])
            dfs(i)
            dfs(i+1)
            l.pop()
            dfs(i+1)
            return res
        dfs(0)
        return list(res for res,_ in itertools.groupby(sorted(res)))
                
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        