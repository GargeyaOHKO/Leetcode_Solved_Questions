class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        d=defaultdict(list)
        for i in roads:
            d[i[0]].append([i[1],i[2]])
            d[i[1]].append([i[0],i[2]])
        seen=set()
        h=[[0,1]]
        mini=float('inf')
        while h:
            cost,curr=heapq.heappop(h)
            if curr in seen:
                continue
            seen.add(curr)
            for i in d[curr]:
                if i[0] not in seen:
                    mini=min(mini,i[1])
                    heapq.heappush(h,[i[1],i[0]])
        return mini


        