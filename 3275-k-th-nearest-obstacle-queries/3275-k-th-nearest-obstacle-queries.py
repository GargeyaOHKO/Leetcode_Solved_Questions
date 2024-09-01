class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        import heapq
        res=[]
        l=[]
        for i in queries:
            s=abs(i[0])+abs(i[1])
            heapq.heappush(l,-s)
            #print(l)
            if len(l)<k:
                res.append(-1)
            elif len(l)>k:
                heapq.heappop(l)
            if len(l)==k:
                res.append(-l[0])
            #print(res)
        return res


        