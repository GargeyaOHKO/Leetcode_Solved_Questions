class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], threshold: int) -> int:
        d=defaultdict(list)
        for i in edges:
            d[i[0]].append([i[1],i[2]])
            d[i[1]].append([i[0],i[2]])
        ans={}
        for i in range(n):
            nodes=0
            #print(0,i,"initial")
            h=[[0,i]]
            seen=set()
            new=set()
            while h:
                #print(h)
                cost,curr=heapq.heappop(h)
                new.add(curr)
                if curr in seen:
                    continue
                seen.add(curr)
                #print(curr)
                for nei,c in d[curr]:
                    if nei not in seen:
                        if cost+c<=threshold:
                            if nei not in new:
                                new.add(nei)
                                nodes+=1
                            heapq.heappush(h,[cost+c,nei])
            if nodes not in ans:
                ans[nodes]=[i]
            else:
                ans[nodes].append(i)
        #print(ans)
        return max(ans[min(ans)])