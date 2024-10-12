class Solution:
    def minGroups(self, inter: List[List[int]]) -> int:
        inter.sort()
        group=[]
        #print(inter)
        for i in inter:
            #print(group)
            if group and i[0]>group[0]:
                e=heapq.heappop(group)
                heapq.heappush(group,i[1])
            else:
                heapq.heappush(group,i[1])
            #print(group)
        return len(group)
        