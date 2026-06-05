class Solution:
    def earliestFinishTime(self, lst: List[int], ld: List[int], wst: List[int], wd: List[int]) -> int:
        land=[]
        water=[]
        for i in range(len(lst)):
            land.append([lst[i],ld[i]])
        for i in range(len(wst)):
            water.append([wst[i],wd[i]])
        land.sort()
        water.sort()

        best=float('inf')
        landbest=float('inf')
        for i in land:
            landbest=min(landbest,i[0]+i[1])
        for i in water:
            if i[0]<=landbest:
                best=min(best,landbest+i[1])
            elif i[0]>landbest:
                best=min(best,i[0]+i[1])

        waterbest=float('inf')
        for i in water:
            waterbest=min(waterbest,i[0]+i[1])
        for i in land:
            if i[0]<=waterbest:
                best=min(best,waterbest+i[1])
            elif i[0]>waterbest:
                best=min(best,i[0]+i[1])
        return best

        
            