class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        po,ao=set(),set()
        moves=[[0,1],[1,0],[0,-1],[-1,0]]
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i==0 or j==0:
                    q=deque()
                    seen=set()
                    q.append([i,j])
                    seen.add((i,j))
                    po.add((i,j))
                    while q:
                        for k in range(len(q)):
                            curr=q.popleft()
                            for m in moves:
                                newr,newc=curr[0]+m[0],curr[1]+m[1]
                                if 0<=newr<len(heights) and 0<=newc<len(heights[0]) and ((newr,newc) not in seen) and heights[newr][newc]>=heights[curr[0]][curr[1]]:
                                    q.append([newr,newc])
                                    seen.add((newr,newc))
                                    po.add((newr,newc))
                if i==len(heights)-1 or j==len(heights[0])-1:
                    q=deque()
                    seen=set()
                    q.append([i,j])
                    seen.add((i,j))
                    ao.add((i,j))
                    while q:
                        for k in range(len(q)):
                            curr=q.popleft()
                            for m in moves:
                                newr,newc=curr[0]+m[0],curr[1]+m[1]
                                if 0<=newr<len(heights) and 0<=newc<len(heights[0]) and ((newr,newc) not in seen) and heights[newr][newc]>=heights[curr[0]][curr[1]]:
                                    q.append([newr,newc])
                                    seen.add((newr,newc))
                                    ao.add((newr,newc))
        #print(ao,po)
        l=[]
        for i in ao:
            if i in po:
                l.append([i[0],i[1]])
        return l