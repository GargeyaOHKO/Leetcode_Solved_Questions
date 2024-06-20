class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res,l=[],[]
        def dfs(i,l,s):
            if i>=len(candidates) or s>target:
                if s==target:
                    res.append(list(l))
                    return None
                return None
            
            l.append(candidates[i])
            dfs(i+1,l,s+candidates[i])
            l.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,l,s)
            return res
        return dfs(0,l,0)
        
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        