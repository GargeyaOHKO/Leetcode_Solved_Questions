class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h=[]
        for i in points:
            x,y=i[0],i[1]
            d=math.pow(i[0],2)+math.pow(i[1],2)
            heapq.heappush(h,[d,i[0],i[1]])
        res=[]
        for z in range(k):
            i=heapq.heappop(h)
            res.append([i[1],i[2]])
            if len(res)==k:
                return res