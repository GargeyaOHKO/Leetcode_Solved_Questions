class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        d=defaultdict(list)
        for r in roads:
            d[r[0]].append([r[1],r[2]])
            d[r[1]].append([r[0],r[2]])
        h=[[0,0]]
        dist=[float('inf')]*n
        ways=[0]*n
        dist[0]=0
        ways[0]=1        
        while h:
            cost,curr=heapq.heappop(h)
            if cost>dist[curr]:
                continue
            for i,w in d[curr]:
                ncost=cost+w
                if ncost<dist[i]:
                    dist[i]=ncost
                    ways[i]=ways[curr]
                    heapq.heappush(h,[ncost,i])
                elif ncost==dist[i]:
                    ways[i]=(ways[i]+ways[curr])%(10**9+7)
        return ways[n-1]


