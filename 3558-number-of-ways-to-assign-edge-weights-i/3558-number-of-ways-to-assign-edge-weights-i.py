class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        d=defaultdict(list)
        for i in edges:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
        q,seen=deque(),set()
        q.append(1)
        seen.add(1)
        c=0
        while q:
            for i in range(len(q)):
                curr=q.popleft()
                for i in d[curr]:
                    if i not in seen:
                        q.append(i)
                        seen.add(i)
            c+=1
        return (2**(c-2))%(10**9+7)