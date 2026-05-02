class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d={}
        for i in range(n+1):
            d[i]=[]
        for i in flights:
            d[i[0]].append([i[1],i[2]])
        heap=[(0,src,0)]
        best={}
        #print(d)
        while heap:
            cost,curr,hop=heapq.heappop(heap)
            #print(cost,curr,hop)
            if hop>k+1:
                continue
            if curr==dst:
                return cost
            if (curr,hop) in best and best[(curr,hop)]<=cost:
                continue
            else:
                best[(curr,hop)]=cost
            for nei,price in d[curr]:
                heapq.heappush(heap,(price+cost,nei,hop+1))
        return -1
            
        