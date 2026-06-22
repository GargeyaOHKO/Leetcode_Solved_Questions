class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        d=defaultdict(list)
        for i in edges:
            d[i[0]].append([i[1],i[2]])
        kt=k
        h=[[0,0,kt-1,labels[0]]]
        seen=set()
        l=[]
        while h:
            cost,curr,kt,alpha=heapq.heappop(h)
            if curr==n-1:
                return cost
            if (curr, kt, alpha) in seen:
                continue
            seen.add((curr, kt, alpha))
            for i in d[curr]:
                if alpha==labels[i[0]]:
                    newkt=kt-1
                    if newkt>=0:
                        heapq.heappush(h,[cost+i[1],i[0],newkt,alpha])
                else:
                    heapq.heappush(h,[cost+i[1],i[0],k-1,labels[i[0]]])
        return -1