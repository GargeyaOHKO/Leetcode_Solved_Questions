class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d={}
        for i in words:
            d[i]=d.get(i,0)+1
        h=[]
        for i in d:
            heapq.heappush(h,[-d[i],i])
        res=[]
        for i in range(k):
            i=heapq.heappop(h)
            res.append(i[1])
        return res