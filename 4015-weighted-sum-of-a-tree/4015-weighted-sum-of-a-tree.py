class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        d=defaultdict(list)
        for i in range(1,len(parent)):
            d[parent[i]].append(i)
        q=deque()
        q.append(0)
        h=0
        while q:
            for i in range(len(q)):
                curr=q.popleft()
                for nxt in d[curr]:
                    q.append(nxt)
            h+=1
        q.append(0)
        res=0
        dpt=1
        while q:
            #print(q)
            for i in range(len(q)):
                curr=q.popleft()
                res+=(nums[curr]*(h-dpt+1))
                if curr in d:
                    for nxt in d[curr]:
                        q.append(nxt)
            dpt+=1
        return res
