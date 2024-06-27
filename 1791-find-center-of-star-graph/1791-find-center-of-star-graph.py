class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d={}
        for i in edges:
            d[i[0]]=d.get(i[0],0)+1
            d[i[1]]=d.get(i[1],0)+1
        m=0
        mx=0
        for i in d:
            if d[i]>m:
                m=d[i]
                mx=i
        return mx