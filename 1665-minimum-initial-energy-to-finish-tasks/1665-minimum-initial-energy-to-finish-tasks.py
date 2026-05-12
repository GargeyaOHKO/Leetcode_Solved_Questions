class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        d=defaultdict(list)
        diff=[]
        s=set()
        for i in tasks:
            d[abs(i[0]-i[1])].append(i)
            if abs(i[0]-i[1]) not in s:
                diff.append(abs(i[0]-i[1]))
                s.add(abs(i[0]-i[1]))
        diff.sort(reverse=True)
        curr=0
        total=0
        for i in diff:
            for j in d[i]:
                #print(j,curr,total)
                if curr<j[1]:
                    temp=j[1]-curr
                    curr+=temp
                    total+=temp
                    curr-=j[0]
                else:
                    curr-=j[0]
        return total

