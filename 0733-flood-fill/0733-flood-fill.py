class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q=deque()
        move=[[1,0],[0,1],[-1,0],[0,-1]]
        q.append([sr,sc])
        seen=set()
        seen.add((sr,sc))
        while q:
            for i in range(len(q)):
                #print(q,seen)
                r,c=q.popleft()
                for j in move:
                    newr=r+j[0]
                    newc=c+j[1]
                    if (newr,newc) not in seen and (newr>=0 and newr<len(image)) and (newc>=0 and newc<len(image[0])):
                        seen.add((newr,newc))
                        if image[newr][newc]==image[sr][sc]:
                            image[newr][newc]=color
                            q.append((newr,newc))
        image[sr][sc]=color
        return image