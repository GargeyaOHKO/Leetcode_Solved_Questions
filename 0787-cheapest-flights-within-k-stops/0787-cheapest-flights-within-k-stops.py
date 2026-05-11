class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d=defaultdict(list)
        for i in flights:
            d[i[0]].append([i[1],i[2]])
        #print(d)
        h=[[0,src,0]]
        seen={}
        while h:
            #print(h,mini,seen)
            cost,curr,hop=heapq.heappop(h)
            if hop>k+1:
                continue
            if curr==dst and hop<=(k+1):
                return cost
            if (curr,hop) in seen and seen[(curr,hop)]<=cost:
                continue
            seen[(curr,hop)]=cost
            for j in d[curr]:
                heapq.heappush(h,[cost+j[1], j[0], hop+1])
        return -1

