class Solution:
    def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:
        d=defaultdict(list)
        for i in edges:
            d[i[0]].append(i[1])
        def dfs(curr):
            if d[curr]==[]:
                return baseTime[curr]
            maxi=float('-inf')
            mini=float('inf')
            for i in d[curr]:
                temp=dfs(i)
                maxi=max(maxi,temp)
                mini=min(mini,temp)
            return maxi+(maxi-mini+baseTime[curr])
        return dfs(0)
