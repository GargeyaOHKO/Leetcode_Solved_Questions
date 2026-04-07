class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        po,ao=set(),set()
        moves=[[0,1],[1,0],[0,-1],[-1,0]]
        q1,q2=deque(),deque()
        seen1,seen2=set(),set()
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i==0 or j==0:
                    q1.append([i,j])
                    seen1.add((i,j))
                    po.add((i,j))
                if i==len(heights)-1 or j==len(heights[0])-1:
                    q2.append([i,j])
                    seen2.add((i,j))
                    ao.add((i,j))
        while q1:
            for k in range(len(q1)):
                curr=q1.popleft()
                for m in moves:
                    newr,newc=curr[0]+m[0],curr[1]+m[1]
                    if 0<=newr<len(heights) and 0<=newc<len(heights[0]) and ((newr,newc) not in seen1) and heights[newr][newc]>=heights[curr[0]][curr[1]]:
                        q1.append([newr,newc])
                        seen1.add((newr,newc))
                        po.add((newr,newc))
        while q2:
            for k in range(len(q2)):
                curr=q2.popleft()
                for m in moves:
                    newr,newc=curr[0]+m[0],curr[1]+m[1]
                    if 0<=newr<len(heights) and 0<=newc<len(heights[0]) and ((newr,newc) not in seen2) and heights[newr][newc]>=heights[curr[0]][curr[1]]:
                        q2.append([newr,newc])
                        seen2.add((newr,newc))
                        ao.add((newr,newc))
        l=[]
        for i in ao:
            if i in po:
                l.append([i[0],i[1]])
        return l