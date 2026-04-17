class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap=[[0,0,0]]
        moves=[[0,1],[0,-1],[1,0],[-1,0]]
        seen=set()
        l=[]
        while heap:
            #print(heap)
            curr,r,c=heapq.heappop(heap)
            if (r,c) in seen:
                continue
            seen.add((r,c))
            if r==len(heights)-1 and c==len(heights[0])-1:
                return curr
            for m in moves:
                newr,newc=m[0]+r,m[1]+c
                if 0<=newr<len(heights) and 0<=newc<len(heights[0]) and (newr,newc) not in seen:
                    seen.add((r,c))
                    diff=max(curr,abs(heights[r][c]-heights[newr][newc]))
                    heapq.heappush(heap,[diff,newr,newc])
                    
