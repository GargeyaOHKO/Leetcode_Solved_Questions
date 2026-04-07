class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        d={}
        inbound=[0 for i in range(len(graph))]
        for i in range(len(graph)):
            for j in graph[i]:
                if j not in d:
                    d[j]=[i]
                else:
                    d[j].append(i)
                inbound[i]+=1
        #print(d)
        #print(inbound)
        q=deque()
        l=[]
        for i in range(len(inbound)):
            if inbound[i]==0:
                q.append(i)
                l.append(i)
        while q:
            for i in range(len(q)):
                #print(q)
                curr=q.popleft()
                #print(curr)
                if curr in d:
                    for j in d[curr]:
                        inbound[j]-=1
                        if inbound[j]==0:
                            q.append(j)
                            l.append(j)
        l.sort()
        return l