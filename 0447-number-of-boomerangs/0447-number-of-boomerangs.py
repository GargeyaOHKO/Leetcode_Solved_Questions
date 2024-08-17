class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        c=0
        for i in points:
            d={}
            for j in points:
                d[(i[0]-j[0])**2+(i[1]-j[1])**2]=d.get((i[0]-j[0])**2+(i[1]-j[1])**2,0)+1
            for i in d:
                if d[i]>1:
                    c+=d[i]*(d[i]-1)
        return c
        