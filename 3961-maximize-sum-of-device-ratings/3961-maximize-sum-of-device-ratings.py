class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        if len(units[0])==1:
            s=0
            for i in units:
                s+=i[0]
            return s

        new=[]
        for i in units:
            i.sort()
            new.append([i[1],i[0]])
        new.sort()
        c=0
        mini=min(new[0][0],new[0][1])
        for i in range(1,len(new)):
            mini=min(mini,new[i][1])
            c+=new[i][0]
        return c+mini


