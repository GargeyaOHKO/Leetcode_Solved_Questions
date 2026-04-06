class Solution:
    def canFinish(self, nc: int, pre: List[List[int]]) -> bool:
        d={i:[] for i in range(nc)}
        inbound=[0 for _ in range(nc)]
        for i in pre:
            d[i[1]].append(i[0])
            inbound[i[0]]+=1
        q=deque()
        for i in range(len(inbound)):
            if inbound[i]==0:
                q.append(i)
        while q:
            for i in range(len(q)):
                curr=q.popleft()
                for j in d[curr]:
                    inbound[j]-=1
                    if inbound[j]==0:
                        q.append(j)
        for i in inbound:
            if i!=0:
                return False
        return True