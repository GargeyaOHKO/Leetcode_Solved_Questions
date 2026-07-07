class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees)<=3:
            return trees
        temp=[]
        for i in trees:
            temp.append([i[1],i[0]])
        temp.sort()
        p0=[temp[0][1],temp[0][0]]
        temp=[]
        for i in trees:
            angle=math.atan2(i[1]-p0[1],i[0]-p0[0])
            dist=math.pow(math.pow(i[1]-p0[1],2)+math.pow(i[0]-p0[0],2),0.5)
            temp.append([angle,dist,i[0],i[1]])
        temp.sort()
        new=[]
        for i in temp:
            new.append([i[2],i[3]])
            while len(new)>2 and ((new[-2][1]-new[-1][1])*(new[-3][0]-new[-2][0]))-((new[-3][1]-new[-2][1])*(new[-2][0]-new[-1][0]))<=0:
                new.pop(-2)
        new.append(new[0])
        add=[]
        #print(new)
        for i in range(len(new)-1):
            A=new[i]
            C=new[i+1]
            for z in trees:
                B=z
                if (C[1]-B[1])*(B[0]-A[0])-(B[1]-A[1])*(C[0]-B[0])==0:
                    add.append(B)
        for i in add:
            new.append(i)
        new=[list(x) for x in set(map(tuple,new))]
        return new

