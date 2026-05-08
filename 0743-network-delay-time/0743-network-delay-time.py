class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d={}
        for i in times:
            if i[0] not in d:
                d[i[0]]=[]
            if i[1] not in d:
                d[i[1]]=[]
            d[i[0]].append([i[1],i[2]])

        h=[[0,k]]
        seen=set()
        maxtime=0
        while h:
            cost,curr=heapq.heappop(h)
            if curr in seen:
                continue
            seen.add(curr)
            maxtime=max(maxtime,cost)
            for j in d[curr]:
                if j[0] not in seen:
                    heapq.heappush(h,[cost+j[1],j[0]])
        if len(seen)==n:
            return maxtime
        return -1