class Solution:
    def minNumberOfSeconds(self, mh: int, wt: List[int]) -> int:
        import heapq
        l=[(t,t,1) for t in wt]
        heapify(l)
        while mh>1:
            #print(l)
            curr,og,mult=heapq.heappop(l)
            heapq.heappush(l,(curr+(og*(mult+1)),og,mult+1)) 
            mh-=1
            #print(l)
        return heappop(l)[0]


        