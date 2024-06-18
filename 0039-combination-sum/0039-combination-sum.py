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
        l=[]
        for i in res:
            if i not in l:
                l.append(i)
        return l
                
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        