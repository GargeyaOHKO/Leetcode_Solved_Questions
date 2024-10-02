class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        l=[]
        d={}
        for i in arr:
            d[i]=d.get(i,0)+1
        d={k:d[k] for k in sorted(d)}
        c=1
        for i in d:
            d[i]=c
            c+=1
        for i in arr:
            l.append(d[i])
        return l
