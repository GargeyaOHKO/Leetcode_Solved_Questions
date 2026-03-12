class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d={}
        c=0
        for i in s:
            if i not in d:
                d[i]=[c,c]
            else:
                start,end=d[i]
                d[i]=[start,c]
            c+=1
        wind=[]
        for i in d:
            wind.append(d[i])
        wind.sort()
        #print(wind)
        start,end=-1,-1
        ends=[]
        for i in range(len(wind)):
            if start==-1:
                start,end=wind[i][0],wind[i][1]
            else:
                if wind[i][0]<end:
                    end=max(end,wind[i][1])
                else:
                    ends.append(end)
                    start,end=wind[i][0],wind[i][1]
        
        ends.append(len(s)-1)
        #print(ends)
        for i in range(len(ends)):
            ends[i]+=1
        for i in range(len(ends)-1,0,-1):
            ends[i]-=ends[i-1]
        return ends

