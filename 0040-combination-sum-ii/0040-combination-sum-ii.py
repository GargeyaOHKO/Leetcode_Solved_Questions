class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res=[]
        def dfs(curr,pos,target):
            if target==0:
                res.append(list(curr))
            if target<0:
                return None
            prev=-1
            for i in range(pos,len(candidates)):
                if candidates[i]==prev:
                    continue
                curr.append(candidates[i])
                dfs(curr,i+1,target-candidates[i])
                curr.pop()
                prev=candidates[i]
            return res
        return dfs([],0,target)
        
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        