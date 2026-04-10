class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        for z in range(len(graph)):
            if graph[z]==[]:
                continue
            odd,even=set(),set()
            q=deque()
            q.append(z)
            odd.add(z)
            k=1
            while q:
                print(q,k,odd,even)
                for i in range(len(q)):
                    curr=q.popleft()
                    for j in graph[curr]:
                        #q.append(j)
                        if k%2==0:
                            if j in even:
                                return False
                            elif j not in odd:
                                odd.add(j)
                                q.append(j)
                        else:
                            if j in odd:
                                return False
                            elif j not in even:
                                even.add(j)
                                q.append(j)
                k+=1
            return True
                        





