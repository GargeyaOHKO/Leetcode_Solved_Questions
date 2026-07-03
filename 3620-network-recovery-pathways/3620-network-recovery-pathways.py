class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        d=defaultdict(list)
        for i in edges:
            d[i[0]].append([i[1],i[2]])
        def dfs(low):
            dist=[float('inf')]*len(online)
            dist[0]=0
            h=[[0,0]]
            while h:
                cost,curr=heapq.heappop(h)
                if cost>dist[curr]:
                    continue
                if cost>k:
                    continue
                if curr==len(online)-1:
                    return True
                for i in d[curr]:
                    if online[i[0]] and i[1]>=low and (cost+i[1])<dist[i[0]]:
                        dist[i[0]]=cost+i[1]
                        heapq.heappush(h,[cost+i[1],i[0]])
            return False

        res=float('-inf')
        l,r=0,(10**9)+1
        while l<=r:
            mid=(l+r)//2
            t=dfs(mid)
            if t==False:
                r=mid-1
            else:
                l=mid+1
                res=max(res,mid)
        if res==float('-inf'):
            return -1
        return res


