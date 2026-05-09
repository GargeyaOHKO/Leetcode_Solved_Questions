class Solution:
    def minGenerations(self, points: List[List[int]], target: List[int]) -> int:
        s=set()
        for i in points:
            s.add((i[0],i[1],i[2]))
        if (target[0],target[1],target[2]) in s:
            return 0
        c=0
        while True:
            new=[]
            for i in range(len(points)):
                for j in range(i+1,len(points)):
                    x,y,z=(points[i][0]+points[j][0])//2,(points[i][1]+points[j][1])//2,(points[i][2]+points[j][2])//2
                    if (x,y,z) not in s:
                        s.add((x,y,z))
                        new.append([x,y,z])
            #print(new)
            c+=1
            if (target[0],target[1],target[2]) in s:
                return c
            if len(new)==0:
                return -1
            else:
                for i in new:
                    points.append(i)
        return -1


